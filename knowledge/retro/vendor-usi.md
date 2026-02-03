# USI (United States Instrument Corporation)

## Models
| Model | Category | Videos Referenced |
|-------|----------|-------------------|
| Pi4 / EV-9031A | Amber CRT Monitor | [KrX3s_Dp7kc] |

## Platform-Specific Knowledge

### USI Pi4 / EV-9031A Amber Monitor

#### Overview
- 9" amber phosphor CRT monitor from 1982 - Source: [KrX3s_Dp7kc]
- Uses composite video input (not TTL) - Source: [KrX3s_Dp7kc]
- Same design as Sanyo VM-4509 (Taiwan Kolin manufactured both) - Source: [KrX3s_Dp7kc]
- Sanyo schematic can be used for USI Pi4 repair - Source: [KrX3s_Dp7kc]

#### Manufacturer
- Taiwan Kolin (OEM manufacturer for both USI and Sanyo) - Source: [KrX3s_Dp7kc]
- Many monitors from this era share the same internal design - Source: [KrX3s_Dp7kc]

#### Front Panel Controls and Switches

##### DC Restoration Switch
- Purpose: Maintains consistent black level regardless of scene content - Source: [KrX3s_Dp7kc]
- Without DC restoration: Bright scenes raise baseline, dark scenes drop baseline - Source: [KrX3s_Dp7kc]
- With DC restoration ON: Black level stays constant, better for general use - Source: [KrX3s_Dp7kc]
- Also called "black level clamping" - Source: [KrX3s_Dp7kc]

##### Inverse Video Switch
- Swaps black and white (negative image) - Source: [KrX3s_Dp7kc]
- Useful for some terminal applications that expected inverse display - Source: [KrX3s_Dp7kc]

##### Impedance Switch (75 Ohm / High-Z)
- 75 Ohm position: Terminates video signal properly (use for single monitor) - Source: [KrX3s_Dp7kc]
- High-Z position: For daisy-chaining multiple monitors (passes signal through) - Source: [KrX3s_Dp7kc]
- Using High-Z with single monitor may cause slightly brighter image but ghosting - Source: [KrX3s_Dp7kc]

#### Common Fault: B+ Voltage Regulator Capacitor

##### Symptoms
- Horizontal interference pattern visible on screen - Source: [KrX3s_Dp7kc]
- Pattern looks like high-frequency ripple superimposed on image - Source: [KrX3s_Dp7kc]
- Most visible in light/bright areas - Source: [KrX3s_Dp7kc]

##### Cause
- Capacitor C607 (220µF 16V) in B+ voltage regulator circuit - Source: [KrX3s_Dp7kc]
- Located near large heatsink that runs hot - Source: [KrX3s_Dp7kc]
- Heat exposure causes capacitor to dry out and lose capacitance - Source: [KrX3s_Dp7kc]
- This capacitor smooths ripple on B+ rail - when it fails, ripple reaches CRT - Source: [KrX3s_Dp7kc]

##### Repair
- Replace C607 with 220µF 16V or higher voltage rating electrolytic - Source: [KrX3s_Dp7kc]
- Can use 25V or 35V rated cap for better heat tolerance - Source: [KrX3s_Dp7kc]
- Consider replacing all electrolytics near heatsink preventatively - Source: [KrX3s_Dp7kc]

#### Power Supply
- B+ voltage regulator provides main power to horizontal output stage - Source: [KrX3s_Dp7kc]
- Linear voltage regulator design (common for era) - Source: [KrX3s_Dp7kc]
- Heatsink gets very hot during normal operation - Source: [KrX3s_Dp7kc]

#### Video Input
- Composite video via BNC connector - Source: [KrX3s_Dp7kc]
- Compatible with Apple II, TRS-80, Commodore, and other composite video sources - Source: [KrX3s_Dp7kc]

#### Related Monitors
- Sanyo VM-4509: Identical internal design, different branding - Source: [KrX3s_Dp7kc]
- Sanyo schematics and service manuals work for USI Pi4 - Source: [KrX3s_Dp7kc]
- Other Taiwan Kolin OEM monitors may share same chassis - Source: [KrX3s_Dp7kc]
