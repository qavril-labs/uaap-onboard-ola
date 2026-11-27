"""Onboard Ola: a UAAP bot, packaged on its own. Installing it registers it with the UAAP kernel."""

from uaap.bots.catalog import BotSpec

SPEC = BotSpec(
    id="onboard-ola",
    name="Onboard Ola",
    version="0.1.0",
    kind="agent",
    module="uaap_bot_onboard_ola.agent",
    class_name="OnboardOla",
    needs_model=True,
    needs_inbox=False,
    summary="Onboarding checklists, equipment and access proposals.",
    examples=(
        "Create first-week onboarding checklist for Jane Doe starting in finance.",
        "Propose system access for John Smith in engineering.",
    ),
)
