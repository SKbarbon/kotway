# IFrame
The `IFrame`  control represents the `<iframe>` (Inline Frame) element, which embeds another HTML page within the current page.

## Properties
### `src: str`
The path or URL of the document to embed.

### `srcdoc: str`
Inline HTML content to show inside the frame (overrides src if both exist).

### `title: str`
A text description of the embedded content. Crucial for accessibility (screen readers).

### `name: str`
A target name for the frame. 

Can be used by `Anchor` control (`<a>` tags) with `target="frame_name"`.

## Triggers
### `add_sandbox_tokens (*tokens: SandboxToken)` and `remove_sandbox_tokens(*tokens: SandboxToken)`
Fire a trigger to add or remove a sandbox token to the control.

### `add_allow_policies` and `remove_allow_policies`
Fire a trigger to add or remove an allow policy.