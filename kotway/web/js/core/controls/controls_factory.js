import {Text} from "./text.js";
import { TextField } from "./textfield.js";
import { Button } from "./button.js";
import { Image } from "./image.js";
import { Container } from "./container.js";
import { Anchor } from "./anchor.js";
import { IFrame } from "./iframe.js";

import { AlertBox } from "./overlays/alertbox.js";
import { PictureInPicture } from "./overlays/pictureinpicture.js";

export const CONTROLS_FACTORY = {
"Text": Text,
"TextField": TextField,
"Button": Button,
"Image": Image,
"Container": Container,
"Anchor": Anchor,
"IFrame": IFrame,

"AlertBox": AlertBox,
"PictureInPicture": PictureInPicture
}