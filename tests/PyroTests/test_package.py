"""
Tests for the package structure and import names.
Also checks if the key API functions are still in place.

Pyro - Python Remote Objects.  Copyright by Irmen de Jong (irmen@razorvine.net).
"""

import unittest
import Pyro4
import Pyro4.constants
import Pyro4.core
import Pyro4.errors
import Pyro4.naming
import Pyro4.nsc
import Pyro4.socketutil
import Pyro4.util


class TestPackage(unittest.TestCase):
    def testPyro4(self):
        self.assertIs(Pyro4.core.Daemon, Pyro4.Daemon)
        self.assertIs(Pyro4.core.Proxy, Pyro4.Proxy)
        self.assertIs(Pyro4.core.URI, Pyro4.URI)
        self.assertIs(Pyro4.core.callback, Pyro4.callback)
        self.assertIs(Pyro4.core.oneway, Pyro4.oneway)
        self.assertIs(Pyro4.core.async, Pyro4.async)
        self.assertIs(Pyro4.core.batch, Pyro4.batch)
        self.assertIs(Pyro4.core.expose, Pyro4.expose)
        self.assertIs(Pyro4.core.behavior, Pyro4.behavior)
        self.assertIs(Pyro4.core.locateNS, Pyro4.locateNS)
        self.assertIs(Pyro4.core.resolve, Pyro4.resolve)
        self.assertIs(Pyro4.core.locateNS, Pyro4.naming.locateNS, "old API function location must still be valid")
        self.assertIs(Pyro4.core.resolve, Pyro4.naming.resolve, "old API function location must still be valid")
        self.assertIsInstance(Pyro4.current_context, Pyro4.core._CallContext)


if __name__ == "__main__":
    unittest.main()
