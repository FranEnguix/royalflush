Quick Start
===========

.. warning::

   This webpage is under construction. We are sorry for the inconvenience.

Before running **Royal FLush**, you need to install and start the XMPP server. We recommend (PyJabber)[https://pyjabber.readthedocs.io] or (Prosody)[https://prosody.im/] with the register in-band enabled.

To run an experiment after installing **Royal FLush**:

.. code-block:: console

Usage: royalflush [OPTIONS] COMMAND [ARGS]...

  Royal FLush CLI

Options:
  --verbose  Enable verbose output.
  --help     Show this message and exit.

Commands:
  analyze-logs     Analyze logs from a previous run inside the given folder.
  create-template  Create a JSON template for the experiment.
  run              Run the main RoyalFlush application with the provided...
  version          Show the current version of RoyalFlush.

.. code-block:: bash

   royalflush run ./test_experiment.json

