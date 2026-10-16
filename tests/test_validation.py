import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('validation', ROOT/'scripts/validate.py')
validation = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validation)


class PackageRegressionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)/'repo'
        self.root.mkdir()
        # Build the distributed package only; never copy private host settings,
        # ignored reference checkouts, environments, or generated user files.
        for relative in ('.agents/skills', '.claude-plugin', 'evals'):
            shutil.copytree(ROOT/relative, self.root/relative)
        for relative in ('README.md', 'CONTRIBUTING.md', 'LICENSE', 'requirements-dev.txt'):
            shutil.copy2(ROOT/relative, self.root/relative)
        self.skill = self.root/'.agents/skills/devtool-agent-readiness'

    def tearDown(self):
        self.temp.cleanup()

    def replace(self, before, after):
        path = self.skill/'SKILL.md'
        path.write_text(path.read_text().replace(before, after))

    def assert_failure(self, text):
        self.assertTrue(any(text in e for e in validation.validate_repository(self.root)))

    def test_valid_distribution(self):
        self.assertEqual([], validation.validate_repository(self.root))

    def test_duplicate_yaml_key_is_not_silently_accepted(self):
        self.replace('license: MIT', 'license: MIT\nlicense: Proprietary')
        self.assert_failure('duplicate frontmatter key')

    def test_directory_and_name_must_match(self):
        self.replace('name: devtool-agent-readiness', 'name: another-skill')
        self.assert_failure('name does not match directory')

    def test_metadata_numbers_need_quoting(self):
        self.replace('version: 2.0.0', 'version: 2')
        self.assert_failure('metadata must contain string')

    def test_missing_bundled_reference_breaks_package(self):
        (self.skill/'references/playbook.md').unlink()
        self.assert_failure('missing local link')

    def test_standalone_skill_cannot_depend_on_sibling(self):
        with (self.skill/'SKILL.md').open('a') as file:
            file.write('\n[Required sibling](../saas-copywriting/SKILL.md)\n')
        self.assert_failure('local link escapes package')

    def test_manifest_must_discover_canonical_files(self):
        path = self.root/'.claude-plugin/plugin.json'
        data = json.loads(path.read_text())
        data['skills'] = ['./missing-skills/']
        path.write_text(json.dumps(data))
        self.assert_failure('plugin must discover')

    def test_missing_readme_inventory_is_detected(self):
        path = self.root/'README.md'
        path.write_text(path.read_text().replace('.agents/skills/devtool-agent-readiness/SKILL.md', 'missing.md'))
        self.assert_failure('skill missing from README')

    def test_stale_release_version_is_detected(self):
        self.replace('version: 2.0.0', 'version: 1.0.0')
        self.assert_failure('skill and plugin versions differ')

    def test_unknown_evaluation_skill_is_detected(self):
        path = self.root/'evals/scenarios.json'
        data = json.loads(path.read_text())
        data[0]['expected_skills'] = ['not-in-this-package']
        path.write_text(json.dumps(data))
        self.assert_failure('evaluation references unknown')

    def test_each_skill_can_be_copied_alone(self):
        for source in (ROOT/'.agents/skills').iterdir():
            if source.is_dir():
                destination = Path(self.temp.name)/'standalone'/source.name
                shutil.copytree(source, destination)
                self.assertEqual([], validation.validate_skill(destination), source.name)


if __name__ == '__main__':
    unittest.main()
