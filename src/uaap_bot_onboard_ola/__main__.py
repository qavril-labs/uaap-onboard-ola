"""Serve this bot, and only this bot, as an MCP server over stdio: `python -m uaap_bot_onboard_ola`."""

import asyncio

from uaap.bots.mcp_server import serve

raise SystemExit(asyncio.run(serve(["onboard-ola"])))
