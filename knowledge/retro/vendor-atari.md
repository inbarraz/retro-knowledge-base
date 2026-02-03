# Atari

## Models
| Model | Category | Videos Referenced |
|-------|----------|-------------------|
| Atari 1200XL | Desktop Computer | [Fm4aLhZtDwk], [GtKhhwhngUI], [xIlxjd82ig0] |
| Atari 800XL | Desktop Computer | [Fm4aLhZtDwk], [GtKhhwhngUI], [zsSiEtSomQI] |
| Atari 600XL | Desktop Computer | [Fm4aLhZtDwk], [GtKhhwhngUI] |
| Atari 800 | Desktop Computer | [Fm4aLhZtDwk], [GtKhhwhngUI] |
| Atari 400 | Desktop Computer | [Fm4aLhZtDwk], [GtKhhwhngUI] |
| Atari 130XE | Desktop Computer | [GtKhhwhngUI], [j-8yycf3ob4] |
| Atari 520 STFM | Desktop Computer | [j-8yycf3ob4] |
| Atari 520 ST | Desktop Computer | [KnTiOoZreD8], [MhKSUXLKuRI] |
| Atari 800 | Desktop Computer | [MIJ_CcdIBJk] |
| Atari 800XL | Desktop Computer | [MIJ_CcdIBJk] |
| Atari C380 Video Pinball | Game Console | [KnTiOoZreD8] |

## Platform-Specific Knowledge

### Atari 1200XL

#### Overview
- Older than 800XL despite model number - Source: [Fm4aLhZtDwk]
- Larger case than 800XL/600XL but similar styling - Source: [Fm4aLhZtDwk]
- Has superior keyboard feel with additional function keys (F1-F4) - Source: [Fm4aLhZtDwk]
- LED indicators: L1, L2, Power - Source: [Fm4aLhZtDwk]
- Function keys and controls along top instead of keyboard edge - Source: [Fm4aLhZtDwk]
- Delete/Backspace key is double-wide (improvement over other Atari keyboards) - Source: [Fm4aLhZtDwk]
- Return key position different from 400/800 and later machines - Source: [Fm4aLhZtDwk]
- Uses AC voltage input with internal voltage regulator despite not needing it - Source: [Fm4aLhZtDwk]
- Brick-style AC power supply retained from 400/800 design - Source: [Fm4aLhZtDwk]
- Relatively rare machine - not many made - Source: [Fm4aLhZtDwk]
- 64KB RAM same as 800XL - Source: [xIlxjd82ig0]
- No PAL version exists - NTSC only - Source: [xIlxjd82ig0]
- Announced Dec 1982, shipped March 1983, discontinued June 1983 - Source: [xIlxjd82ig0]
- Only on market for approximately 4 months - Source: [xIlxjd82ig0]
- Launch price $899 (originally announced at $1000) - Source: [xIlxjd82ig0]
- Has unique Help key (not on other Atari 8-bit machines) - Source: [xIlxjd82ig0]
- Joystick ports reduced to 2 (from 4 on 400/800) - Source: [xIlxjd82ig0]
- Extra joystick lines repurposed for RAM banking - Source: [xIlxjd82ig0]

#### Market Failure
- Press criticized high price at launch - Source: [xIlxjd82ig0]
- Could not compete with cheaper Commodore 64/VIC-20 - Source: [xIlxjd82ig0]
- Atari 400/800 production costs still too high - Source: [xIlxjd82ig0]
- Led to development of cost-reduced 600XL and 800XL - Source: [xIlxjd82ig0]
- 1400XL and 1450XL (with disk drives) shown but never released - Source: [xIlxjd82ig0]

#### L1/L2 LED Indicators
- Unique feature not on other Atari 8-bits - Source: [xIlxjd82ig0]
- Change state during RAM bank switching - Source: [xIlxjd82ig0]
- Visible during self-test RAM testing - Source: [xIlxjd82ig0]

#### Built-In Diagnostics
- Press Help key at Atari logo to enter diagnostics - Source: [xIlxjd82ig0]
- Different from 800XL (Option key on 800XL) - Source: [xIlxjd82ig0]
- Tests: Memory, Audio, Video, Keyboard - Source: [xIlxjd82ig0]
- Audio test: Goes through all 4 sound channels - Source: [xIlxjd82ig0]
- Keyboard test: Hit keys to verify all register - Source: [xIlxjd82ig0]

#### Physical Layout
- Angled joystick ports on left side - unique design - Source: [xIlxjd82ig0]
- Cartridge slot very deep - cartridge sits flush - Source: [xIlxjd82ig0]
- No parallel I/O port (unlike 800 and 600) - Source: [xIlxjd82ig0]
- Power switch on left side - Source: [xIlxjd82ig0]
- RF channel selector on back - Source: [xIlxjd82ig0]
- 9V AC power input (same as 400/800 and disk drives) - Source: [xIlxjd82ig0]

#### CPU
- Uses Sally CPU (CO14806) - NOT a standard 6502 - Source: [Fm4aLhZtDwk]
- Cannot substitute regular 6502 without adapter board with extra logic - Source: [Fm4aLhZtDwk]
- Sally is embedded/modified 6502 variant - Source: [Fm4aLhZtDwk]

#### Chips
- GTIA: 14805 version-1 - Source: [Fm4aLhZtDwk]
- ANTIC: 21697 (ANTIC E, later version for NTSC) - Source: [Fm4aLhZtDwk]
- Older ANTIC is 12296 - Source: [Fm4aLhZtDwk]
- ANTIC B is for PAL machines - Source: [Fm4aLhZtDwk]
- MMU: CO61618, made by MMI (PAL chip manufacturer) - Source: [Fm4aLhZtDwk]
- POKEY for sound - Source: [Fm4aLhZtDwk]
- 64KB of RAM (Mtech chips in original video) - Source: [Fm4aLhZtDwk]

#### Original Boot Behavior
- Normal 1200XL boots to rainbow scrolling Fuji symbol (no cartridge installed) - Source: [Fm4aLhZtDwk]
- Does NOT have built-in BASIC like 800XL - Source: [Fm4aLhZtDwk]
- Option key during boot puts into diagnostic mode - Source: [Fm4aLhZtDwk]
- 400/800 boot to "memo pad" notepad application - Source: [Fm4aLhZtDwk]

#### Common ROM Swap Modification
- Very common to swap 800XL ROMs into 1200XL - Source: [Fm4aLhZtDwk]
- Provides built-in BASIC (not present originally) - Source: [Fm4aLhZtDwk]
- Improves software compatibility - Source: [Fm4aLhZtDwk]
- Requires bodge wires on ROM chips and bottom of board - Source: [Fm4aLhZtDwk]
- Two flying leads on basic ROM (pins bent out) - Source: [Fm4aLhZtDwk]
- Additional wiring on bottom side to PIA and MMU - Source: [Fm4aLhZtDwk]
- OS ROM is 16KB (271128/231128 equivalent) - Source: [Fm4aLhZtDwk]
- Basic ROM is 8KB (2364 equivalent) - Source: [Fm4aLhZtDwk]
- MMU involved in ROM bank switching - Source: [Fm4aLhZtDwk]
- Some people add switch to toggle between original and 800XL ROMs - Source: [Fm4aLhZtDwk]
- 800XL ROMs recommended to keep on all time for compatibility - Source: [Fm4aLhZtDwk]

#### Keyboard
- Mitsumi keyboard - same manufacturer as many Commodore 64 keyboards - Source: [Fm4aLhZtDwk]
- Very similar feel to Mitsumi C64 keyboard - Source: [Fm4aLhZtDwk]
- Double-shot keycaps (high quality) - Source: [Fm4aLhZtDwk]
- Springs under each key - Source: [Fm4aLhZtDwk]
- Carbon-impregnated rubber pieces press on PCB traces - Source: [Fm4aLhZtDwk]
- Has ICs and capacitors on keyboard PCB (unusual for keyboards) - Source: [Fm4aLhZtDwk]

##### Keyboard Servicing
- Very easy to service: Remove all screws, PCB comes out without removing keys - Source: [Fm4aLhZtDwk]
- Clean dust and debris with IPA - Source: [Fm4aLhZtDwk]
- For non-working keys: Can use remote control repair paint (conductive) on rubber contacts - Source: [Fm4aLhZtDwk]

##### Keycap/Slider Compatibility
- Keycaps compatible with Commodore 64 keys (same cross-point mount) - Source: [Fm4aLhZtDwk]
- C64 keycaps can be used on 1200XL if missing/broken - Source: [Fm4aLhZtDwk]
- Key sliders appear similar to C64 sliders - Source: [Fm4aLhZtDwk]
- Springs are different between C64 and 1200XL - Source: [Fm4aLhZtDwk]
- C64 keyboards and parts are abundant - useful for 1200XL repairs - Source: [Fm4aLhZtDwk]

#### Video Output

##### DIN Jack Issues
- Video DIN jack prone to bad solder joints - Source: [Fm4aLhZtDwk]
- Symptoms: flaky video, cutting in and out when touching connector - Source: [Fm4aLhZtDwk]
- First try DeoxIT cleaning - may just be dirty contacts - Source: [Fm4aLhZtDwk]
- If still flaky after cleaning: desolder and inspect/replace jack - Source: [Fm4aLhZtDwk]
- Thin traces on PCB can break - may need bodge wires - Source: [Fm4aLhZtDwk]
- Check for broken traces under solder mask - may need to expose copper with Dremel - Source: [Fm4aLhZtDwk]

##### DIN Jack Replacement
- "Conom" brand replacement jacks available - Source: [Fm4aLhZtDwk]
- Use blue tack to hold jack in place during soldering - Source: [Fm4aLhZtDwk]
- After replacement, connection should be firm with no wiggle - Source: [Fm4aLhZtDwk]

##### S-Video Modification
- Chroma hole on DIN jack may not be plated on 1200XL - Source: [Fm4aLhZtDwk]
- Wire must be soldered directly to pin - Source: [Fm4aLhZtDwk]
- Route chroma wire away from other video signals to prevent dot patterns - Source: [Fm4aLhZtDwk]
- Can place tape to hold wire in position along ground plane - Source: [Fm4aLhZtDwk]
- S-video mod can include switch to enable/disable composite - Source: [Fm4aLhZtDwk]
- Disabling composite circuit eliminates dot crawl in S-video output - Source: [Fm4aLhZtDwk]
- Disabling composite also disables RF modulator - Source: [Fm4aLhZtDwk]
- Can connect luma to composite pin so composite cable shows B&W image - Source: [Fm4aLhZtDwk]

##### "Clear Pic" Mod (Bob Woolly)
- Display upgrade for fuzzy 1200XL - Source: [Fm4aLhZtDwk]
- Changes multiple component values - Source: [Fm4aLhZtDwk]
- R63 changed to 1 ohm - Source: [Fm4aLhZtDwk]
- L15 changed from inductor to 1 ohm resistor - Source: [Fm4aLhZtDwk]
- Various capacitor removals - Source: [Fm4aLhZtDwk]
- 75 ohm resistors added (termination adjustment) - Source: [Fm4aLhZtDwk]
- R24: 130 ohms, leave blank - Source: [Fm4aLhZtDwk]

##### Color Phase Adjustment
- Potentiometer on motherboard adjusts color phase - Source: [Fm4aLhZtDwk]
- Use color bar test pattern to adjust - Source: [Fm4aLhZtDwk]
- SALT (Super Atari Language Toolkit) cartridge has color bar test - Source: [Fm4aLhZtDwk]
- A8 Pico Cart H multicart can run SALT for testing - Source: [Fm4aLhZtDwk]
- Adjust so bottom color bars have smooth gradation to next color - Source: [Fm4aLhZtDwk]
- Test with known games like Miss Pac-Man for correct colors - Source: [Fm4aLhZtDwk]

#### Hardware Quirks
- Heat sink has notch cut to clear capacitor C47 - Source: [Fm4aLhZtDwk]
- Bridge rectifier package is oversized for power consumption - Source: [Fm4aLhZtDwk]
- Angled joystick ports - joystick sticks out side of case (nice design touch) - Source: [Fm4aLhZtDwk]
- Serial number and date code on case bottom - Source: [Fm4aLhZtDwk]

### Atari 800

#### Overview
- Tank-like build quality - extremely robust construction - Source: [GtKhhwhngUI]
- Heavy metal RF shielding throughout - Source: [GtKhhwhngUI]
- Socketed everything - very serviceable - Source: [GtKhhwhngUI]
- Considered most reliable Atari 8-bit machine - Source: [GtKhhwhngUI]
- Modular design with separate RAM/ROM modules - Source: [GtKhhwhngUI]
- Card-based architecture - RAM comes on cards that slot into motherboard - Source: [MIJ_CcdIBJk]
- Early models had 48K RAM (three 16K RAM cards) - Source: [MIJ_CcdIBJk]
- Very early units had 8K base, upgraded with additional cards - Source: [MIJ_CcdIBJk]

#### Video Quality
- Has excellent video quality - Luma/Chroma works right out of the box - Source: [Fm4aLhZtDwk]
- No modification needed for S-video output - Source: [Fm4aLhZtDwk]
- Later machines (600XL, 800XL, 1200XL) have worse video than 800 - Source: [Fm4aLhZtDwk]

#### Self-Test Diagnostic Mode
- Hold Option key during power-on to enter self-test - Source: [MIJ_CcdIBJk]
- Tests RAM, ROM, keyboard, and other components - Source: [MIJ_CcdIBJk]
- Same diagnostic mode works on 800XL and other 8-bit Ataris - Source: [MIJ_CcdIBJk]

#### Keyboard Variants
- Two distinct keyboard types exist - Source: [MIJ_CcdIBJk]
- Early Stackpole switches - mechanical with individual switches - Source: [MIJ_CcdIBJk]
- Later membrane keyboard - cost-reduced design - Source: [MIJ_CcdIBJk]
- Stackpole keyboard considered superior typing feel - Source: [MIJ_CcdIBJk]
- Can identify by looking under keycaps at switch mechanism - Source: [MIJ_CcdIBJk]

#### Reliability
- Most reliable of all Atari 8-bit models - Source: [GtKhhwhngUI]
- Socketed chips rarely fail - easy to diagnose and replace - Source: [GtKhhwhngUI]
- Full-size keyboard mechanism is durable - Source: [GtKhhwhngUI]
- Power supply issues more common than motherboard failures - Source: [GtKhhwhngUI]

### Atari 400

#### Overview
- Entry-level Atari 8-bit computer - Source: [GtKhhwhngUI]
- Membrane keyboard (not mechanical) - Source: [GtKhhwhngUI]
- 16KB RAM standard (expandable) - Source: [GtKhhwhngUI]
- Same video/audio capabilities as 800 - Source: [GtKhhwhngUI]

#### Keyboard
- Flat membrane keyboard widely disliked - Source: [GtKhhwhngUI]
- Common to replace with mechanical keyboard upgrade - Source: [GtKhhwhngUI]
- Some users adapt 800 keyboards to 400 - Source: [GtKhhwhngUI]

### Atari 600XL

#### Overview
- Compact XL-series machine - Source: [GtKhhwhngUI]
- 16KB RAM standard (limitation) - Source: [GtKhhwhngUI]
- No composite video monitor jack (RF only by default) - Source: [GtKhhwhngUI]
- Cartridge port on top - Source: [GtKhhwhngUI]

#### Limitations
- 16KB RAM insufficient for many programs - Source: [GtKhhwhngUI]
- Memory expansion required for most software - Source: [GtKhhwhngUI]
- Less expansion options than 800XL - Source: [GtKhhwhngUI]

### Atari 800XL

#### Overview
- Most common Atari 8-bit computer - Source: [GtKhhwhngUI]
- 64KB RAM standard - Source: [GtKhhwhngUI], [MIJ_CcdIBJk]
- Built-in BASIC - Source: [GtKhhwhngUI], [MIJ_CcdIBJk]
- Best software compatibility of XL line - Source: [GtKhhwhngUI]
- Cost-reduced design compared to 800 - Source: [MIJ_CcdIBJk]

#### Self-Test Diagnostic Mode
- Hold Option key during power-on to enter self-test - Source: [MIJ_CcdIBJk]
- Displays color bars and tests various components - Source: [MIJ_CcdIBJk]
- Press keyboard keys to verify keyboard matrix - Source: [MIJ_CcdIBJk]
- Tests RAM, ROM, GTIA, POKEY, and other chips - Source: [MIJ_CcdIBJk]

#### Reliability Notes
- Generally reliable but less robust than 800 - Source: [GtKhhwhngUI]
- Some custom chips (GTIA, ANTIC, POKEY) not socketed - Source: [GtKhhwhngUI]
- Bad capacitors can develop over time - Source: [GtKhhwhngUI]
- Video quality varies between revisions - Source: [GtKhhwhngUI]

#### Video Modifications
- Luma/Chroma mod recommended for S-video - Source: [GtKhhwhngUI]
- UAV (Ultimate Atari Video) board popular upgrade - Source: [GtKhhwhngUI]
- Cleaner output than stock composite - Source: [GtKhhwhngUI]

#### Keyboard Variants
- Multiple keyboard types exist for 800XL - Source: [zsSiEtSomQI]
- AWC Type 2 keyboard: mechanical with sliders and switches on PCB - Source: [zsSiEtSomQI]
- Keyboard variants documented at: forums.atariage.com/topic/105170 - Source: [zsSiEtSomQI]
- Some keyboards have excellent feel, others are "terrible" - Source: [zsSiEtSomQI]
- Quality varies significantly between keyboard types - Source: [zsSiEtSomQI]

#### Keyboard Washing (AWC Type 2)

##### When Keycaps Won't Come Off
- Some AWC Type 2 keyboards have stuck keycaps - Source: [zsSiEtSomQI]
- Even with keycap removal tool, caps feel like they'll break switches - Source: [zsSiEtSomQI]
- May have been glued by previous owner - Source: [zsSiEtSomQI]
- If caps won't come off, can't apply DeoxIT to switches directly - Source: [zsSiEtSomQI]

##### Washing Procedure
- Remove keyboard from computer - Source: [zsSiEtSomQI]
- Wash under running warm tap water with brush and soap - Source: [zsSiEtSomQI]
- Dirty keyboards release dark liquid when washed - Source: [zsSiEtSomQI]
- Key binding may improve while wet (water lubricates) - Source: [zsSiEtSomQI]

##### Ultrasonic Cleaning
- Submerge keyboard in ultrasonic cleaner after initial wash - Source: [zsSiEtSomQI]
- Keep ribbon cable out of water if possible - Source: [zsSiEtSomQI]
- Run 15+ minutes - water heats to ~40°C - Source: [zsSiEtSomQI]
- Rinse in plain water after ultrasonic to remove soap - Source: [zsSiEtSomQI]
- Push keys repeatedly while submerged to pump out soapy water - Source: [zsSiEtSomQI]
- Ultrasonic cleaning can revive non-working switches - Source: [zsSiEtSomQI]

##### Water Hardness Considerations
- Soft water (like Portland, Oregon) doesn't leave mineral deposits - Source: [zsSiEtSomQI]
- Hard water areas: Soak in distilled water after washing to displace tap water - Source: [zsSiEtSomQI]
- Let fully dry before reassembly to avoid mineral deposits in switches - Source: [zsSiEtSomQI]

##### Drying
- Blow off water with compressed air - Source: [zsSiEtSomQI]
- Place in sun or over heating vent (not directly on heat source) - Source: [zsSiEtSomQI]
- Allow multiple days for complete drying - Source: [zsSiEtSomQI]
- Water inside switches acts as temporary lubricant while wet - Source: [zsSiEtSomQI]

##### Post-Washing Results
- Keys may bind again after drying (no lubrication) - Source: [zsSiEtSomQI]
- Some switches may become worse after cleaning - Source: [zsSiEtSomQI]
- Other switches that weren't working may start working - Source: [zsSiEtSomQI]
- Pressing keys repeatedly can revive marginal switches - Source: [zsSiEtSomQI]
- Keys feel smooth (not gritty) after cleaning - Source: [zsSiEtSomQI]
- Cosmetically much improved - visible dirt removed from between keys - Source: [zsSiEtSomQI]

##### Keyboard Lubrication
- Proper fix for binding: disassemble and add switch lubricant - Source: [zsSiEtSomQI]
- Requires removing keycaps (impossible if stuck) - Source: [zsSiEtSomQI]
- Special keyboard switch lubricant available - Source: [zsSiEtSomQI]
- Ultrasonic cleaning with soap removes original lubricant - Source: [zsSiEtSomQI]

#### Keyboard Trace Repair
- Broken PCB traces can cause entire rows/columns to fail - Source: [zsSiEtSomQI]
- Check keyboard matrix to identify row/column patterns - Source: [zsSiEtSomQI]
- If multiple keys on same row/column fail, likely trace not switch - Source: [zsSiEtSomQI]
- If scattered keys fail, likely individual switches - Source: [zsSiEtSomQI]
- Shift keys are wired together - if one works, trace is good - Source: [zsSiEtSomQI]
- Test switch continuity with multimeter on PCB back - Source: [zsSiEtSomQI]
- Add bodge wires to repair broken traces - Source: [zsSiEtSomQI]
- Follow trace visually to find break point - Source: [zsSiEtSomQI]

#### Ribbon Cable
- Keyboard ribbon cable is extremely fragile - Source: [zsSiEtSomQI]
- Metal fingers on connector can come unglued and wiggle - Source: [zsSiEtSomQI]
- Handle with extreme care to avoid folding/breaking - Source: [zsSiEtSomQI]

### Atari 1200XL

#### Reliability Issues
- Least reliable Atari 8-bit computer - Source: [GtKhhwhngUI]
- Software compatibility problems with original ROM - Source: [GtKhhwhngUI]
- Many units have bad custom chips - Source: [GtKhhwhngUI]
- Video DIN jack notorious for cold solder joints - Source: [GtKhhwhngUI]
- Relatively rare - fewer produced than other models - Source: [GtKhhwhngUI]

### Atari 130XE

#### Overview
- Final Atari 8-bit computer (XE series) - Source: [GtKhhwhngUI]
- 128KB RAM with bank switching - Source: [GtKhhwhngUI], [j-8yycf3ob4]
- Enhanced graphics modes with extra RAM - Source: [GtKhhwhngUI]
- ECI (Enhanced Cartridge Interface) port - Source: [GtKhhwhngUI]
- End of the Atari 8-bit line - Source: [j-8yycf3ob4]
- Modern styling that matches Atari ST line - Source: [j-8yycf3ob4]

#### PAL vs NTSC
- Significant differences between PAL and NTSC versions - Source: [GtKhhwhngUI]
- PAL machines have different ANTIC chip revision - Source: [GtKhhwhngUI]
- Some software region-locked - Source: [GtKhhwhngUI]
- PAL has more scanlines (different timing) - Source: [GtKhhwhngUI]

#### Keyboard
- Different keyboard feel from 800XL - Source: [GtKhhwhngUI]
- Some consider keyboard inferior to XL series - Source: [GtKhhwhngUI]
- Plunger-style keys rather than full travel - Source: [GtKhhwhngUI]
- Keyboard membrane commonly fails over time - Source: [j-8yycf3ob4]
- Membrane failure is most common 130XE issue - Source: [j-8yycf3ob4]

### Atari 520 ST

#### Overview
- Original Atari ST with 512KB RAM - Source: [KnTiOoZreD8], [MhKSUXLKuRI]
- External power supply (brick style) - Source: [KnTiOoZreD8]
- No built-in floppy drive (external drive required) - Source: [KnTiOoZreD8]

#### 4MB RAM Upgrade

##### Native 4MB Support
- 520 ST MMU chip already supports 4MB addressing - Source: [MhKSUXLKuRI]
- Just needs additional RAM and one address line connected - Source: [MhKSUXLKuRI]
- No MMU replacement required - hardware capability exists - Source: [MhKSUXLKuRI]

##### Old Marpet-Style RAM Expansions (NOT Recommended)
- Old RAM expansions used PLCC socket adapters - Source: [MhKSUXLKuRI]
- Clip-on adapters damage 68-pin PLCC sockets over time - Source: [MhKSUXLKuRI]
- Zigzag PLCC sockets basically impossible to find - Source: [MhKSUXLKuRI]
- Damaged socket means difficult/expensive repair - Source: [MhKSUXLKuRI]

##### STRam Open Source RAM Expansion (Recommended)
- Modern open source 4MB RAM expansion - Source: [MhKSUXLKuRI]
- GitHub: github.com/agranlund/STRam - Source: [MhKSUXLKuRI]
- Solders into RAM chip holes instead of using PLCC sockets - Source: [MhKSUXLKuRI]
- Does not stress or damage PLCC sockets - Source: [MhKSUXLKuRI]
- Requires removing original RAM chips - Source: [MhKSUXLKuRI]
- Requires running one bodge wire for address line 9 (A9) - Source: [MhKSUXLKuRI]
- Much safer long-term solution - Source: [MhKSUXLKuRI]

### Atari 520 STFM

#### Overview
- 16/32-bit computer based on Motorola 68000 CPU - Source: [j-8yycf3ob4]
- ST = Sixteen/Thirty-two (bit) - Source: [j-8yycf3ob4]
- FM = Built-in RF modulator - Source: [j-8yycf3ob4]
- Internal floppy drive (unlike original 520 ST) - Source: [j-8yycf3ob4]
- Internal power supply (unlike external brick on some models) - Source: [j-8yycf3ob4]

#### Memory
- 512KB RAM standard - Source: [j-8yycf3ob4]
- Can be upgraded to 1MB RAM with modification - Source: [j-8yycf3ob4]
- Uses DRAM chips that can be piggybacked or replaced - Source: [j-8yycf3ob4]

#### Known Issues
- Keys yellow unevenly over time - Source: [j-8yycf3ob4]
- Some keys turn yellow while others stay original color - Source: [j-8yycf3ob4]
- Uneven yellowing due to different plastic batches - Source: [j-8yycf3ob4]
- Retrobrite can help but results vary - Source: [j-8yycf3ob4]

#### Floppy Drive
- Built-in 3.5" double-density floppy drive - Source: [j-8yycf3ob4]
- 720KB capacity per disk - Source: [j-8yycf3ob4]
- External floppy port for additional drives - Source: [j-8yycf3ob4]

#### RF Modulator
- Built-in RF output for TV connection - Source: [j-8yycf3ob4]
- Useful for users without dedicated monitor - Source: [j-8yycf3ob4]
- Also has monitor output for better quality - Source: [j-8yycf3ob4]

#### Historical Context
- Part of Atari ST line (1985-1993) - Source: [j-8yycf3ob4]
- Competitor to Commodore Amiga - Source: [j-8yycf3ob4]
- Popular in Europe, especially UK and Germany - Source: [j-8yycf3ob4]
- Strong MIDI support made it popular with musicians - Source: [j-8yycf3ob4]

## Reliability Ranking (Most to Least Reliable)
1. Atari 800 - tank-like construction, fully socketed - Source: [GtKhhwhngUI]
2. Atari 800XL - solid but cost-reduced vs 800 - Source: [GtKhhwhngUI]
3. Atari 130XE - generally reliable but later production - Source: [GtKhhwhngUI]
4. Atari 600XL - reliable but limited - Source: [GtKhhwhngUI]
5. Atari 400 - membrane keyboard failure prone - Source: [GtKhhwhngUI]
6. Atari 1200XL - least reliable, compatibility issues - Source: [GtKhhwhngUI]

### Atari Video Cables

#### Compatibility
- Commodore 64 S-video cables work with modded Atari computers - Source: [Fm4aLhZtDwk]
- Same DIN pinout can be used - Source: [Fm4aLhZtDwk]

## Tools & Equipment

### Diagnostic Tools
- A8 Pico Cart H: Multicart for Atari 8-bit - Source: [Fm4aLhZtDwk]
- SALT (Super Atari Language Toolkit): System testing including color bars - Source: [Fm4aLhZtDwk]
- SALT CPS (Super Salt): More comprehensive diagnostics - Source: [Fm4aLhZtDwk]

### Video Testing
- RetroTink for upscaling S-video to HDMI - Source: [Fm4aLhZtDwk]
- RetroTink has auto-gain that can make video issues look better than they are - Source: [Fm4aLhZtDwk]

### Atari C380 Video Pinball

#### Overview
- Pre-2600 Atari game console (1977) - Source: [KnTiOoZreD8]
- Predecessor to Atari 2600 - Source: [KnTiOoZreD8]
- Wood grain finish (faux) with brown plastic body - Source: [KnTiOoZreD8]
- Based on "Pong on a chip" single-chip design - Source: [KnTiOoZreD8]
- Essentially a 2600 without cartridge slot with built-in ROMs - Source: [KnTiOoZreD8]

#### Games
- Multiple built-in pinball-style games - Source: [KnTiOoZreD8]
- Breakout-type game included - Source: [KnTiOoZreD8]
- Select button changes games - Source: [KnTiOoZreD8]
- Option and Reset buttons available - Source: [KnTiOoZreD8]

#### Controls
- Paddle controller on unit - Source: [KnTiOoZreD8]
- Five buttons on top - Source: [KnTiOoZreD8]
- Side buttons for pinball flippers - Source: [KnTiOoZreD8]
- Flippers have timed operation (can't hold indefinitely) - Source: [KnTiOoZreD8]

#### Power
- Takes 6 C-cell batteries - Source: [KnTiOoZreD8]
- Uses same power supply as Atari 2600 - Source: [KnTiOoZreD8]

#### Video Output
- Original RF output - Source: [KnTiOoZreD8]
- Can be composite modded - Source: [KnTiOoZreD8]
- Video levels may be low after composite mod - Source: [KnTiOoZreD8]
- Audio levels may also be low after mod - Source: [KnTiOoZreD8]

### Atari ST Custom IC Reference

#### Shifter (Video Chip)
- Part number: CO25913-38 - Source: [KnTiOoZreD8]
- Also CO25914-38A variant - Source: [KnTiOoZreD8]
- Handles video output - Source: [KnTiOoZreD8]

#### DMA Controller
- Part number: CO25913-38 (different marking series) - Source: [KnTiOoZreD8]
- Also CO25913-20 variant - Source: [KnTiOoZreD8]

#### Glue Chip (Logic Integration)
- Part number: CO25915-38 (PLCC package) - Source: [KnTiOoZreD8]
- Connects different motherboard components together - Source: [KnTiOoZreD8]
- "Glue logic" term comes from this function - Source: [KnTiOoZreD8]

#### MMU (Memory Management Unit)
- Part number: CO25912-38 - Source: [KnTiOoZreD8]
- Also CO25912-20 variant - Source: [KnTiOoZreD8]
- Dash number may not indicate significant difference - Source: [KnTiOoZreD8]
- PLCC package - Source: [KnTiOoZreD8]

#### Sound Chip
- YM2149F - Source: [KnTiOoZreD8]
- Standard Yamaha sound chip - Source: [KnTiOoZreD8]

#### Floppy Controller
- WD1772 - Source: [KnTiOoZreD8]
- Western Digital standard controller - Source: [KnTiOoZreD8]

#### Keyboard Processor
- Part number: CO22-002 - Source: [KnTiOoZreD8]
- Installed on keyboard PCB - Source: [KnTiOoZreD8]

#### Boot ROM (Original ST)
- Part number: CO26034-29 - Source: [KnTiOoZreD8]
- Early STs had minimal boot ROM - Source: [KnTiOoZreD8]
- Required TOS to be loaded from floppy into RAM - Source: [KnTiOoZreD8]
- Later machines had TOS in ROM on motherboard - Source: [KnTiOoZreD8]

#### TOS ROM
- Part number: CO26160-001 (TOS 1.0 ROM High 2) - Source: [KnTiOoZreD8]
- TOS 1.04 common on later machines - Source: [KnTiOoZreD8]
- Six ROM chips in full TOS set - Source: [KnTiOoZreD8]

#### PLCC Sockets (Zigzag)
- Atari ST uses unusual PLCC sockets - Source: [KnTiOoZreD8]
- Pins are zigzag pattern instead of standard rows - Source: [KnTiOoZreD8]
- 68-pin PLCC - Source: [KnTiOoZreD8]
- Basically impossible to find - Source: [KnTiOoZreD8]
- Same sockets used for Mac accelerators that clip onto 68000 - Source: [KnTiOoZreD8]

#### IC Reference Resource
- Best Electronics website has comprehensive Atari IC list - Source: [KnTiOoZreD8]
- URL: best-electronics-ca.com/custom-i.htm - Source: [KnTiOoZreD8]

## Common Issues Summary

### 1200XL Specific
1. Flaky DIN video jack (bad solder joints) - Source: [Fm4aLhZtDwk]
2. Color phase off (adjust potentiometer) - Source: [Fm4aLhZtDwk]
3. No built-in BASIC (common ROM swap mod) - Source: [Fm4aLhZtDwk]
4. Software incompatibility vs 800XL (ROM swap fixes) - Source: [Fm4aLhZtDwk]
