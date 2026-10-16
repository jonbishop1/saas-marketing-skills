"""Host transport success and content quality must never be conflated."""
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('runner', ROOT/'scripts/run_behavior.py')
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


class BehavioralEvidenceTests(unittest.TestCase):
    def record(self, host_result):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            plugin = base/'plugin'
            (plugin/'.claude-plugin').mkdir(parents=True)
            (plugin/'.claude-plugin/plugin.json').write_text('{"name":"fixture-plugin"}')
            skill = plugin/'.agents/skills/example'
            skill.mkdir(parents=True)
            (skill/'SKILL.md').write_text('Fixture skill instructions')
            case = dict(id='test-case', expected_skills=['example'], prompt='Facts only.',
                        must_include=['Requested artifact'], must_avoid=['Invented claims'])

            def host(*args, **kwargs):
                kwargs['stdout'].write(json.dumps(dict(type='system', subtype='init', model='fixture-model'))+'\n')
                kwargs['stdout'].write(json.dumps(dict(type='result', **host_result))+'\n')
                return subprocess.CompletedProcess(args[0], 0)

            output = base/'private-results'
            output.mkdir()
            with patch.object(runner.subprocess, 'run', side_effect=host):
                return runner.run_case(case, plugin, output, 10)

    def test_successful_response_still_requires_quality_review(self):
        result = self.record(dict(is_error=False, result='A plausible but unreviewed answer.'))
        self.assertTrue(result['host_success'])
        self.assertEqual(result['quality_verdict'], 'unreviewed')
        self.assertEqual(result['model'], 'fixture-model')
        self.assertEqual(len(result['entrypoint_sha256']), 64)

    def test_limit_response_is_not_counted_as_completed_behavior(self):
        result = self.record(dict(is_error=True, result="You've hit your session limit."))
        self.assertFalse(result['host_success'])
        self.assertEqual(result['quality_verdict'], 'unreviewed')
        self.assertIn('session limit', result['output'])


if __name__ == '__main__':
    unittest.main()
