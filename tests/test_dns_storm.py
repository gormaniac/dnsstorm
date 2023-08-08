import os

import synapse.tests.utils as s_test

dirname = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

class DnsStormTest(s_test.StormPkgTest):

    assetdir = os.path.join(dirname, 'tests/testassets')
    pkgprotos = (os.path.join(dirname, 'dnsstorm.yaml'),)

    async def test_dns_queries(self):

        async with self.getTestCore() as core:

            queries = [
                "gormo.dns --query google.com",
                "gormo.dns --query google.com --type NS",
                "gormo.dns --query google.com --type MX",
                "gormo.dns --query google.com --type TXT",
                "gormo.dns --query google.com --type AAAA",
                # TODO Get working examples of these
                # "gormo.dns --query dns.google --type PTR",
                # "gormo.dns --query google.com --type CNAME",
            ]

            for query in queries:
                msgs = await core.stormlist(query)
                print([m[1] for m in msgs if m[0] == 'node'])
                self.stormHasNoWarnErr(msgs)
