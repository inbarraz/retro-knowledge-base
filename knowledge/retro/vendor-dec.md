# Digital Equipment Corporation (DEC)

## Models
| Model | Category | Videos Referenced |
|-------|----------|-------------------|
| PC 320P | Laptop | [4uxKHjXGXnU] |
| LK-401 | ANSI Keyboard | [LdI0e8rNbdY] |
| DEC Rainbow | Desktop Computer | [LdI0e8rNbdY] |
| VT-220 | Video Terminal | [RneTw_LThzQ] |
| VT-100 | Video Terminal | [rO7mpa6eo5U] |
| VT-100 AVO | Expansion Board | [rO7mpa6eo5U] |

## Platform-Specific Knowledge

### DEC PC 320P Laptop

#### Overview
- 386 SX laptop from 1991 (based on date codes) - Source: [4uxKHjXGXnU]
- CPU in socket (unusual for laptops) - Source: [4uxKHjXGXnU]
- 2MB RAM (4x Panasonic chips, 4-bit wide each) - Source: [4uxKHjXGXnU]
- Assembled in USA - Source: [4uxKHjXGXnU]

#### Ports
- VGA connector - Source: [4uxKHjXGXnU]
- Serial port - Source: [4uxKHjXGXnU]
- Parallel port - Source: [4uxKHjXGXnU]
- External keyboard connector (possibly keyboard + mouse) - Source: [4uxKHjXGXnU]
- Docking station alignment pin on back - Source: [4uxKHjXGXnU]
- Modem add-on slot on side - Source: [4uxKHjXGXnU]

#### Power
- 16V external power input - Source: [4uxKHjXGXnU]
- Main battery: 12V 1.4Ah NiMH or NiCad - Source: [4uxKHjXGXnU]
- Battery has 4 pins: two for power, two for thermal sense - Source: [4uxKHjXGXnU]
- Fully charged battery is ~14V - Source: [4uxKHjXGXnU]

#### Known Issues
- Battery packs leak badly (typical for NiCad/NiMH of era) - Source: [4uxKHjXGXnU]
- Electrolytic caps all over motherboard leak (multiple sizes: 100µF/6V, 22µF/25V, 47µF/16V, 10µF/50V) - Source: [4uxKHjXGXnU]
- Resume battery (internal standby battery) leaks - used for RAM refresh during battery swap - Source: [4uxKHjXGXnU]
- Dallas RTC chip will need battery replacement - Source: [4uxKHjXGXnU]
- Cold cathode backlit screen may be dim - Source: [4uxKHjXGXnU]
- Inverter may need service - Source: [4uxKHjXGXnU]

#### Disassembly Notes
- Screen screws on one side hold computer together - Source: [4uxKHjXGXnU]
- Battery compartment hides expansion interface (possibly math coprocessor socket) - Source: [4uxKHjXGXnU]
- Motherboard extends under keyboard - Source: [4uxKHjXGXnU]
- Internal IDE hard drive (full height) - Source: [4uxKHjXGXnU]
- Standard floppy drive - Source: [4uxKHjXGXnU]

#### Battery Pack Repair
- CAUTION: Only open dead packs, do it outside, be prepared for fire - Source: [4uxKHjXGXnU]
- Contains thermal sensor/diode for temperature monitoring - Source: [4uxKHjXGXnU]
- Fusible resistor for protection - Source: [4uxKHjXGXnU]
- Cannot just replace with lithium cells without additional protection circuitry - Source: [4uxKHjXGXnU]
- Do NOT plug in to charge unless cells are replaced with compatible chemistry - Source: [4uxKHjXGXnU]

### DEC Rainbow

#### Overview
- Dual CPU desktop computer (Z80 and 8088) - Source: [LdI0e8rNbdY]
- Can run CP/M-80, CP/M-86, and MS-DOS - Source: [LdI0e8rNbdY]
- Popular in business environments in early 1980s - Source: [LdI0e8rNbdY]

#### Compatible Keyboards
- LK-401 ANSI keyboard works with DEC Rainbow - Source: [LdI0e8rNbdY]
- Uses RJ11 or RJ12 connector (telephone-style modular jack) - Source: [LdI0e8rNbdY]
- Same keyboard family used across multiple DEC systems - Source: [LdI0e8rNbdY]

### LK-401 ANSI Keyboard

#### Overview
- DEC keyboard with ANSI layout - Source: [LdI0e8rNbdY]
- Part of LK-40x keyboard family - Source: [LdI0e8rNbdY]
- Serial communication protocol (not PS/2 or AT compatible) - Source: [LdI0e8rNbdY]

#### Connector
- RJ11 or RJ12 modular jack (telephone-style connector) - Source: [LdI0e8rNbdY]
- Different from most PC keyboards of the era - Source: [LdI0e8rNbdY]
- Allows keyboard to be located away from computer - Source: [LdI0e8rNbdY]

#### Compatibility
- Works with DEC Rainbow - Source: [LdI0e8rNbdY]
- May work with other DEC systems using same protocol - Source: [LdI0e8rNbdY]
- Not directly compatible with IBM PC without adapter/converter - Source: [LdI0e8rNbdY]

### DEC VT-220 Terminal

#### Overview
- Video terminal from DEC, successor to VT-100 - Source: [RneTw_LThzQ]
- Built-in emulation modes for VT-100, VT-52 compatibility - Source: [RneTw_LThzQ]
- Available in amber, green, or white phosphor versions - Source: [RneTw_LThzQ]
- Serial communication (RS-232) at various baud rates - Source: [RneTw_LThzQ]
- 132 column mode supported - Source: [RneTw_LThzQ]

#### Phosphor Color Identification
- Use UV flashlight (365nm) to identify phosphor type - Source: [RneTw_LThzQ]
- Amber phosphor: Glows purple/violet under UV light - Source: [RneTw_LThzQ]
- Green phosphor: Glows bright green under UV light - Source: [RneTw_LThzQ]
- White phosphor: Glows white/grayish under UV light - Source: [RneTw_LThzQ]
- Useful for identifying tubes when powered off - Source: [RneTw_LThzQ]

#### Serial Port Settings
- Supports baud rates up to 19200 - Source: [RneTw_LThzQ]
- Common settings: 9600 baud, 8N1 (8 data bits, no parity, 1 stop bit) - Source: [RneTw_LThzQ]
- Configure via terminal setup menus - Source: [RneTw_LThzQ]

#### Emulation Modes
- VT-220 native mode: Full feature set - Source: [RneTw_LThzQ]
- VT-100 mode: Compatibility with older software - Source: [RneTw_LThzQ]
- VT-52 mode: Legacy compatibility - Source: [RneTw_LThzQ]
- Mode selection via setup menu - Source: [RneTw_LThzQ]

#### 132 Column Mode
- Terminal can switch between 80 and 132 columns - Source: [RneTw_LThzQ]
- Used for wide spreadsheets, databases - Source: [RneTw_LThzQ]
- Software can send escape sequence to change mode - Source: [RneTw_LThzQ]
- Characters smaller in 132 column mode - Source: [RneTw_LThzQ]

#### CRT Cataracts (Safety Glass Degradation)
- DEC terminals have laminated safety glass over CRT face - Source: [RneTw_LThzQ]
- Glue layer between glass and CRT can degrade over time - Source: [RneTw_LThzQ]
- Degradation appears as milky/cloudy patches or yellowing - Source: [RneTw_LThzQ]
- Called "cataracts" due to visual similarity to eye condition - Source: [RneTw_LThzQ]
- Affects visibility but terminal still functions - Source: [RneTw_LThzQ]
- Repair requires removing safety glass (tricky, potential CRT damage) - Source: [RneTw_LThzQ]
- Some collectors prefer cataracts over risking CRT during removal - Source: [RneTw_LThzQ]

#### ZiModem WiFi Modem Connection
- ZiModem: ESP8266-based WiFi serial modem - Source: [RneTw_LThzQ]
- Connects to VT-220 serial port via null modem cable - Source: [RneTw_LThzQ]
- Provides internet access for serial terminals - Source: [RneTw_LThzQ]
- Can connect to BBS systems, telnet hosts - Source: [RneTw_LThzQ]
- Configure baud rate to match terminal settings - Source: [RneTw_LThzQ]
- Hayes-compatible AT command set - Source: [RneTw_LThzQ]

#### Setup Menu Access
- Press Setup key to enter configuration mode - Source: [RneTw_LThzQ]
- Navigate with arrow keys - Source: [RneTw_LThzQ]
- Save settings to NVRAM - Source: [RneTw_LThzQ]
- Reset to defaults option available - Source: [RneTw_LThzQ]

### DEC VT-100 Terminal

#### Overview
- Classic video terminal, industry standard for terminal emulation - Source: [rO7mpa6eo5U]
- Introduced 1978, defined the "VT-100" standard - Source: [rO7mpa6eo5U]
- Base model is 80-column only - Source: [rO7mpa6eo5U]
- Advanced Video Option (AVO) adds features - Source: [rO7mpa6eo5U]

#### Built-in Self Test and Error Codes
- VT-100 has diagnostic self-test at power-on - Source: [rO7mpa6eo5U]
- Error codes displayed as numbers on screen - Source: [rO7mpa6eo5U]
- Codes indicate specific subsystem failures - Source: [rO7mpa6eo5U]
- AVO-related errors show when option board has problems - Source: [rO7mpa6eo5U]

### VT-100 Advanced Video Option (AVO) Board

#### Overview
- Optional expansion board for VT-100 terminals - Source: [rO7mpa6eo5U]
- Plugs into motherboard inside terminal - Source: [rO7mpa6eo5U]
- Adds 132-column mode and character attributes - Source: [rO7mpa6eo5U]

#### Added Features
- 132 column mode (vs base 80 columns) - Source: [rO7mpa6eo5U]
- Bold character display - Source: [rO7mpa6eo5U]
- Underline attribute - Source: [rO7mpa6eo5U]
- Blinking characters - Source: [rO7mpa6eo5U]
- Reverse video attribute - Source: [rO7mpa6eo5U]
- Double-width/double-height characters - Source: [rO7mpa6eo5U]

#### Key Components
- 2114 SRAM chips (1K x 4-bit static RAM) - Source: [rO7mpa6eo5U]
- SRAM stores character attributes - Source: [rO7mpa6eo5U]
- Additional SRAM needed for 132-column mode (more characters per line) - Source: [rO7mpa6eo5U]
- Multiple 2114 chips on board - Source: [rO7mpa6eo5U]

#### Troubleshooting AVO Issues

##### Symptom Analysis
- Garbled attributes = SRAM or data path issue - Source: [rO7mpa6eo5U]
- Missing 132-column mode = board not recognized - Source: [rO7mpa6eo5U]
- Diagnostic error codes point to specific failures - Source: [rO7mpa6eo5U]

##### Oscilloscope Diagnostics
- Probe data lines (D0-D7) on 2114 chips - Source: [rO7mpa6eo5U]
- Compare signals between working and suspect chips - Source: [rO7mpa6eo5U]
- Look for stuck or missing signals - Source: [rO7mpa6eo5U]
- Data lines should show activity during operation - Source: [rO7mpa6eo5U]

##### Connector Problems
- AVO board connects to motherboard via edge connector - Source: [rO7mpa6eo5U]
- Poor pin contact can cause intermittent failures - Source: [rO7mpa6eo5U]
- Check for bent or corroded connector pins - Source: [rO7mpa6eo5U]
- One bad pin can affect entire data bus - Source: [rO7mpa6eo5U]

##### Connector Cleaning
- DeoxIT D100 (concentrate) for connector contacts - Source: [rO7mpa6eo5U]
- Apply to edge connector fingers - Source: [rO7mpa6eo5U]
- Clean mating connector on motherboard - Source: [rO7mpa6eo5U]
- Reseat board several times to work cleaner into contacts - Source: [rO7mpa6eo5U]

##### Bodge Wire Repair
- If specific connector pin remains unreliable after cleaning - Source: [rO7mpa6eo5U]
- Can run wire from board trace directly to motherboard - Source: [rO7mpa6eo5U]
- Bypasses unreliable connector contact - Source: [rO7mpa6eo5U]
- Find trace that goes to problem pin, solder wire, route to motherboard - Source: [rO7mpa6eo5U]
- Permanent repair for connector wear - Source: [rO7mpa6eo5U]

#### 2114 SRAM Testing
- 2114 is 1024 x 4-bit static RAM - Source: [rO7mpa6eo5U]
- 18-pin DIP package - Source: [rO7mpa6eo5U]
- Can test with SRAM tester or piggyback method - Source: [rO7mpa6eo5U]
- Failures may be single bit or entire chip - Source: [rO7mpa6eo5U]
- Still available as NOS or modern replacements - Source: [rO7mpa6eo5U]
