# uaap-onboard-ola

**Onboard Ola** (agent bot, a model): Onboarding checklists, equipment and access proposals.

This bot runs on the UAAP kernel, [qavril-labs/uaap](https://github.com/qavril-labs/uaap). Installing this
package registers it with the kernel through the `uaap.bots` entry point, so the kernel's service, CLI and
MCP server pick it up.

```
pip install "uaap-onboard-ola @ git+https://github.com/qavril-labs/uaap-onboard-ola.git"
python -m uaap.bots describe onboard-ola
```

In code:

```python
from uaap.bots import BotHost
host = BotHost(tools=register_my_tools, model=my_model)
bot = host.build("onboard-ola")
```

Develop: `pip install -e ".[dev]"`, then `ruff check .` and `pytest`.
The test doubles come from the kernel (`uaap.testing`). The agent standard is in the kernel's docs;
`tests/test_conformance.py` checks this bot against it.
