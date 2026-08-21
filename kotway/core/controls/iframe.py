from ...models.controldefaultkwargs import ControlDefaultKwargs, Unpack
from .control import Control, ElementPropType
from ...models import SandboxToken, AllowPolicy

class IFrame (Control):
    """The `<iframe>` (Inline Frame) element embeds another HTML page within the current page."""
    def __init__ (self, src: str = None, 
                  srcdoc: str = None,
                  title: str = None,
                  name: str = None,
                  *args, **kwargs: Unpack[ControlDefaultKwargs]):
        super().__init__(*args, **kwargs)

        self.src = src
        self.srcdoc = srcdoc
        self.title = title
        self.name = name


    def add_sandbox_tokens (self, *tokens: SandboxToken):
        """Fire a trigger to add a sandbox token to the control."""
        for token in tokens:
            self.__modify_sandbox_tokens(token, "add")

    def remove_sandbox_tokens (self, *tokens: SandboxToken):
        """Fire a trigger to remove a sandbox token from the control."""
        for token in tokens:
            self.__modify_sandbox_tokens(token, "remove")

    def __modify_sandbox_tokens (self, token: SandboxToken, action: str):
        """Trigger worker for trigger name: 'modify_sandbox_tokens'
        
        ARGS:
            token (`SandboxToken`): A sanbox token.
            action (`string`): A value of "add" or "remove".
        """
        self._execute_trigger("modify_sandbox_tokens", {"token": token, "action": action})


    def add_allow_policies (self, *policies: AllowPolicy):
        """Fire a trigger to add an allow policy."""
        for policy in policies:
            self.__modify_allow_policies(policy, "add")

    def remove_allow_policies (self, *policies: AllowPolicy):
        """Fire a trigger to remove an allow policy."""
        for policy in policies:
            self.__modify_allow_policies(policy, "remove")


    def __modify_allow_policies (self, policy: AllowPolicy, action: str):
        """Trigger worker for trigger name: 'modify_allow_policies'
        
        ARGS:
            token (`SandboxToken`): A sanbox token.
            action (`string`): A value of "add" or "remove".
        """
        self._execute_trigger("modify_allow_policies", {"policy": policy, "action": action})

    # == Properties ==

    @property
    def src (self) -> str:
        """The path or URL of the document to embed."""
        return self._get_prop_value(ElementPropType.PROP, "src")

    @src.setter
    def src (self, value: str):
        self._set_prop_value(ElementPropType.PROP, "src", value)

    @property
    def srcdoc (self) -> str:
        """Inline HTML content to show inside the frame (overrides src if both exist)."""
        return self._get_prop_value(ElementPropType.PROP, "srcdoc")

    @srcdoc.setter
    def srcdoc (self, value: str):
        self._set_prop_value(ElementPropType.PROP, "srcdoc", value)


    @property
    def title (self) -> str:
        """A text description of the embedded content. Crucial for accessibility (screen readers)."""
        return self._get_prop_value(ElementPropType.PROP, "title")

    @title.setter
    def title (self, value: str):
        self._set_prop_value(ElementPropType.PROP, "title", value)


    @property
    def name (self) -> str:
        """A target name for the frame. 
        Can be used by `Anchor` control (`<a>` tags) with `target="frame_name"`."""
        return self._get_prop_value(ElementPropType.PROP, "name")

    @name.setter
    def name (self, value: str):
        self._set_prop_value(ElementPropType.PROP, "name", value)