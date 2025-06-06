from .domain import (
    Size,
    Dimension,
    TextElement,
    Video,
    VideoProperties,
    VideoSourceType,
    RgbColor,
    Color,
    ThemeColorType,
    SolidFill,
    ShapeBackgroundFill,
    OutlineFill,
    Weight,
    Outline,
    DashStyle,
    ShadowTransform,
    BlurRadius,
    Shadow,
    ShadowType,
    RectanglePosition,
    ShapeProperties,
    CropProperties,
    ColorStop,
    RecolorName,
    Recolor,
    ImageProperties,
    PropertyState,
    StretchedPictureFill,
    PageBackgroundFill,
    AutoText,
    AutoTextType,
    MasterProperties,
    NotesProperties,
    PageType,
    PredefinedLayout,
    ColorScheme,
    ThemeColorPair,
    Line,
    LineProperties,
    WordArt,
    SheetsChart,
    SheetsChartProperties,
    SpeakerSpotlight,
    SpeakerSpotlightProperties,
    Group,
)
from .presentation import Presentation
from .page import Page, LayoutProperties, SlidePageProperties
from .element import ElementKind
from .credentials import initialize_credentials

# Import SlidePageProperties as PageProperties for backward compatibility
PageProperties = SlidePageProperties
