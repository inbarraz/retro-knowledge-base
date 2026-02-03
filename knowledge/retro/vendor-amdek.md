# Amdek

## Models
| Model | Category | Videos Referenced |
|-------|----------|-------------------|
| Video 300A | Composite Amber Monitor | [7blLes8Vgbs] |
| 310A | MDA/Hercules Monitor | [7blLes8Vgbs] |

## Platform-Specific Knowledge

### Amdek Video 300A

#### Overview
- Composite video amber CRT monitor - Source: [7blLes8Vgbs]
- Popular for Apple II and other 8-bit computers - Source: [7blLes8Vgbs]
- 12" CRT, runs at 13.2kV high voltage - Source: [7blLes8Vgbs]
- Amdek was US company but monitors were OEM sourced - Source: [7blLes8Vgbs]
- 120V/220V selectable via switch - Source: [7blLes8Vgbs]
- No power LED - Source: [7blLes8Vgbs]

#### Anti-Glare Mesh
- Cloth mesh filter (like pantyhose material) over glossy CRT - Source: [7blLes8Vgbs]
- Dirt passes through mesh to CRT, dims picture - Source: [7blLes8Vgbs]
- Must disassemble monitor completely to clean underneath - Source: [7blLes8Vgbs]
- Many owners just remove mesh entirely - Source: [7blLes8Vgbs]

#### Construction
- Isolated transformer design (not hot chassis) - Source: [7blLes8Vgbs]
- Safe to connect to grounded computers - Source: [7blLes8Vgbs]
- No schematics or service manual available - Source: [7blLes8Vgbs]
- Front panel painted brown plastic - scratches easily - Source: [7blLes8Vgbs]

#### Common Failures

##### Brown Glue Damage
- Brown glue used to stabilize components during shipping - Source: [7blLes8Vgbs]
- Becomes corrosive and conductive over time - Source: [7blLes8Vgbs]
- Destroys components it contacts (diodes, inductors, capacitors) - Source: [7blLes8Vgbs]
- Check for brown glue as first troubleshooting step - Source: [7blLes8Vgbs]

##### Shorted Zener Diode in Cathode Drive
- 1N4xxx zener diode in cathode drive circuit can short - Source: [7blLes8Vgbs]
- Symptom: No video on screen but horizontal oscillator works (15.7kHz audible) - Source: [7blLes8Vgbs]
- Symptom: Cathode voltage stuck at ~60V instead of showing video waveform - Source: [7blLes8Vgbs]
- Diode shorts from brown glue corrosion - Source: [7blLes8Vgbs]
- Part number unknown (1N4xxx series zener, voltage unmarked) - Source: [7blLes8Vgbs]
- 33V zener worked as replacement - Source: [7blLes8Vgbs]

### 310A
- MDA/Hercules version with 9-pin connector - Source: [7blLes8Vgbs]
- Physically identical to 300A - Source: [7blLes8Vgbs]

## Repair Techniques

### Cathode Drive Troubleshooting
- Video signal should show ~25V peak-to-peak on cathode - Source: [7blLes8Vgbs]
- Classic two-transistor output design - Source: [7blLes8Vgbs]
- Can't see waveform between the two transistors (current-based, not voltage) - Source: [7blLes8Vgbs]
- Video signal visible on input and emitter of first transistor - Source: [7blLes8Vgbs]
- If cathode shows flat ~60V, check diode/resistor in collector circuit - Source: [7blLes8Vgbs]

### Quick Diagnostics
- 15.7kHz horizontal oscillator audible (use spectrum analyzer app) - Source: [7blLes8Vgbs]
- Wrong frequency indicates horizontal circuit problem - Source: [7blLes8Vgbs]
- High voltage present = horizontal deflection working - Source: [7blLes8Vgbs]
- Heater voltage should be ~12V - Source: [7blLes8Vgbs]
- Heater resistance ~75 ohms - Source: [7blLes8Vgbs]
