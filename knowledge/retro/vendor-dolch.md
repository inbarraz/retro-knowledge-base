# Dolch

## Models
| Model | Category | Videos Referenced |
|-------|----------|-------------------|
| PAC-62 | Portable PC | [LJhsSpxJtXc] |

## Platform-Specific Knowledge

### Dolch PAC-62 Portable Computer

#### Overview
- Luggable/portable PC form factor - Source: [LJhsSpxJtXc]
- SuperSocket 7 motherboard with AMD K6-2 500MHz CPU - Source: [LJhsSpxJtXc]
- Built-in LCD screen (original was smaller/lower resolution) - Source: [LJhsSpxJtXc]
- PCI slots available for expansion - Source: [LJhsSpxJtXc]
- No AGP slot (Super Socket 7 limitation) - Source: [LJhsSpxJtXc]

#### iPad 3 Screen Upgrade Project
- iPad 3 Retina display (2048x1536) can be used as replacement LCD - Source: [LJhsSpxJtXc]
- Uses LCD controller board that accepts VGA or DVI input - Source: [LJhsSpxJtXc]
- Higher resolution and quality than original Dolch screen - Source: [LJhsSpxJtXc]
- 9.7" diagonal matches form factor reasonably well - Source: [LJhsSpxJtXc]

#### DOS Text Mode Problem

##### The Issue
- DOS text mode (720x400 at 70Hz) not displaying properly - Source: [LJhsSpxJtXc]
- LCD controller board doesn't recognize this resolution over VGA - Source: [LJhsSpxJtXc]
- Screen shows as unsupported or incorrect - Source: [LJhsSpxJtXc]
- Windows works fine (640x480 and higher) - Source: [LJhsSpxJtXc]

##### Why It Happens
- VGA signal is analog, timing can vary between cards - Source: [LJhsSpxJtXc]
- 720x400@70Hz is oddball resolution used only by DOS text mode - Source: [LJhsSpxJtXc]
- Many LCD scalers don't support this specific timing - Source: [LJhsSpxJtXc]
- DVI is digital with stricter timing spec, more reliable - Source: [LJhsSpxJtXc]

##### DVI Solution
- Use video card with DVI output - Source: [LJhsSpxJtXc]
- DVI carries same timings but digital signal - Source: [LJhsSpxJtXc]
- LCD controller handles DVI DOS text mode correctly - Source: [LJhsSpxJtXc]
- GeForce 6200 PCI card with DVI works perfectly - Source: [LJhsSpxJtXc]

#### Video Card Options

##### GeForce 6200 PCI
- PCI version (not PCIe or AGP) - Source: [LJhsSpxJtXc]
- Has both VGA and DVI outputs - Source: [LJhsSpxJtXc]
- Works in PAC-62's PCI slots - Source: [LJhsSpxJtXc]
- Full DOS compatibility with DVI - Source: [LJhsSpxJtXc]
- Supports CRT and LCD simultaneously - Source: [LJhsSpxJtXc]

##### AGP Card Issues (General)
- PAC-62 has no AGP slot (Super Socket 7) - Source: [LJhsSpxJtXc]
- AGP cards have different keying for voltage variants - Source: [LJhsSpxJtXc]
- 3.3V only cards won't fit 1.5V AGP slots and vice versa - Source: [LJhsSpxJtXc]
- Universal AGP cards work in either slot type - Source: [LJhsSpxJtXc]
- ATI Radeon 9600 SE is 1.5V/0.8V only, incompatible with older AGP - Source: [LJhsSpxJtXc]

#### Super Socket 7 Platform Notes
- Final evolution of Socket 7 standard - Source: [LJhsSpxJtXc]
- 100MHz front side bus - Source: [LJhsSpxJtXc]
- Supports AMD K6-2, K6-III, and Cyrix processors - Source: [LJhsSpxJtXc]
- No AGP support (AGP came with Slot 1/Socket 370) - Source: [LJhsSpxJtXc]
- PCI only for graphics cards - Source: [LJhsSpxJtXc]

## LCD Controller Boards for Retro Use

### VGA vs DVI Input Considerations

#### VGA Limitations
- Analog signal quality varies by card and cable - Source: [LJhsSpxJtXc]
- Unusual resolutions may not be recognized - Source: [LJhsSpxJtXc]
- DOS text mode (720x400@70Hz) often problematic - Source: [LJhsSpxJtXc]
- Some controllers have poor analog-to-digital conversion - Source: [LJhsSpxJtXc]

#### DVI Advantages
- Digital signal, no analog conversion artifacts - Source: [LJhsSpxJtXc]
- Stricter timing specification, better compatibility - Source: [LJhsSpxJtXc]
- DOS text mode works reliably over DVI - Source: [LJhsSpxJtXc]
- HDMI electrically compatible (use adapter) - Source: [LJhsSpxJtXc]

### iPad Screen Conversion

#### iPad 3 Retina Display
- 2048x1536 resolution (3:4 aspect ratio) - Source: [LJhsSpxJtXc]
- High pixel density looks excellent - Source: [LJhsSpxJtXc]
- Controller boards available from various sources - Source: [LJhsSpxJtXc]
- Need matching controller for specific iPad model - Source: [LJhsSpxJtXc]

#### Controller Board Selection
- Must match iPad panel model exactly - Source: [LJhsSpxJtXc]
- Get board with VGA AND DVI/HDMI for best compatibility - Source: [LJhsSpxJtXc]
- Audio pass-through useful for some builds - Source: [LJhsSpxJtXc]
- OSD (on-screen display) controls for adjustment - Source: [LJhsSpxJtXc]
