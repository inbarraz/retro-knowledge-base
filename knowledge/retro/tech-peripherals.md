# Keyboards, Joysticks, Sound Cards, and Connector Techniques

> Part of the retro knowledge base. See also: tech-*.md files for other categories.

## Contents
- [PC Sound Cards](#pc-sound-cards)
- [DIN Jack Repair](#din-jack-repair)
- [Keyboard Repair](#keyboard-repair)
- [Vintage Connectors and Cables](#vintage-connectors-and-cables)
- [Joysticks and Controllers](#joysticks-and-controllers)

## PC Sound Cards

### Creative Sound Blaster CT1305B (Sound Blaster 1.5/2.0)
- Earlier Sound Blaster model with sockets for CMS (Creative Music System) chips - Source: [taoG-JnkSZI]
- CMS uses two Phillips SAA1099 chips plus a GAL - Source: [taoG-JnkSZI]
- Reproduction GAL files available now that algorithms have been figured out - Source: [taoG-JnkSZI]
- SAA1099 chips available from AliExpress - Source: [taoG-JnkSZI]
- Has real Yamaha OPL FM synthesis chip - Source: [taoG-JnkSZI]
- CMS provides 22 channels of stereo sine wave sound (Nintendo-style) - Source: [taoG-JnkSZI]
- Perfect for XT or 286 era systems - Source: [taoG-JnkSZI]
- Cards from early 1992 based on date codes - Source: [taoG-JnkSZI]
- Very reliable cards (unusual for one not to work) - Source: [taoG-JnkSZI]

### Creative Sound Blaster 16 CT1740
- Non-plug-and-play version with jumpers for configuration - Source: [taoG-JnkSZI]
- Has real Yamaha OPL3 chip for authentic FM synthesis - Source: [taoG-JnkSZI]
- Interface connector for Creative CD-ROM (not standard IDE) - Source: [taoG-JnkSZI]
- Note: Sound Blasters with standard IDE can be used with XT-IDE BIOS on 286 systems - Source: [taoG-JnkSZI]
- Wave Blaster expansion port for wavetable daughter boards - Source: [taoG-JnkSZI]

### Yamaha DB50XG Wavetable Daughter Board
- Plugs into Wave Blaster port on Sound Blaster cards - Source: [taoG-JnkSZI]
- Released 1996, adds polyphonic MIDI/wavetable synthesis - Source: [taoG-JnkSZI]
- 16-32 note polyphony depending on sound complexity - Source: [taoG-JnkSZI]
- Based on same synthesizer chips as Yamaha MU50, MU80, QS300 keyboard - Source: [taoG-JnkSZI]
- 12MB of sounds compressed to 4MB ROM - Source: [taoG-JnkSZI]
- 672 sounds and 21 drum kits total - Source: [taoG-JnkSZI]
- XG mode: 480 melodic sounds and 11 drum kits - Source: [taoG-JnkSZI]
- XG is Yamaha's answer to Roland GS standard - Source: [taoG-JnkSZI]
- General MIDI compatible with added variations and digital effects - Source: [taoG-JnkSZI]
- Align pins carefully when installing (easy to misalign) - Source: [taoG-JnkSZI]

### Ensoniq Soundscape S-2000
- Made by Ensoniq Corporation (founders from Commodore) - Source: [taoG-JnkSZI]
- 1994 card with Motorola 68000 processor at 8MHz - Source: [taoG-JnkSZI]
- Same CPU as Macintosh Classic on a sound card - Source: [taoG-JnkSZI]
- Onboard memory for loading samples - Source: [taoG-JnkSZI]
- Prone to SMD capacitor leakage (MUST recap before use) - Source: [taoG-JnkSZI]
- After recap: works perfectly as Windows 3.1/95 sound card - Source: [taoG-JnkSZI]
- General MIDI sounds good - Source: [taoG-JnkSZI]
- Sound Blaster and AdLib emulation is poor (bad for DOS games) - Source: [taoG-JnkSZI]
- Best suited for games with native General MIDI support - Source: [taoG-JnkSZI]
- Can recap with ceramic caps (twist method successful) - Source: [taoG-JnkSZI]

### STB Ultrasound 32 Pro (Compaq Interwave GUS)
- OEM Gravis Ultrasound card for Compaq systems - Source: [taoG-JnkSZI]
- Uses Interwave chip (later revision of GUS technology) - Source: [taoG-JnkSZI]
- Known for early death/reliability issues - Source: [taoG-JnkSZI]
- Cards often stopped working after years of use - Source: [taoG-JnkSZI]
- Requires modified ROM and combination of Interwave + older GUS drivers - Source: [taoG-JnkSZI]
- MegaM (Sound Blaster/AdLib emulation) may not work - Source: [taoG-JnkSZI]
- As GUS card: functional but may have clicking in some programs - Source: [taoG-JnkSZI]
- Mixer chip different from standard GUS - normal drivers don't control it - Source: [taoG-JnkSZI]
- Interwave drivers needed for mixer (Windows 95 primarily) - Source: [taoG-JnkSZI]
- Volume defaults to zero without proper Interwave driver - Source: [taoG-JnkSZI]
- Vogons thread has comprehensive guide and all needed files - Source: [taoG-JnkSZI]

### Gravis Ultrasound (General)
- Wave table synthesis with sample loading capability - Source: [taoG-JnkSZI]
- Similar architecture to Amiga (hardware channels with sample playback) - Source: [taoG-JnkSZI]
- More channels and memory than Amiga - Source: [taoG-JnkSZI]
- Very rare and expensive today - Source: [taoG-JnkSZI]
- Required for certain demos on original hardware - Source: [taoG-JnkSZI]

### ATI VGA Wonder 16
- Combination TTL 9-pin digital output AND VGA on same card - Source: [taoG-JnkSZI]
- Software-controlled output selection - Source: [taoG-JnkSZI]
- Supports: CGA, EGA, VGA, multisync, monochrome monitors - Source: [taoG-JnkSZI]
- 256KB RAM fully populated - Source: [taoG-JnkSZI]
- Not a fast card but very compatible - Source: [taoG-JnkSZI]
- No schematics available, difficult to troubleshoot - Source: [taoG-JnkSZI]
- Everything goes through bus transceiver to main IC - Source: [taoG-JnkSZI]

### Sound Card Testing Tips
- CubicPlayer good for testing MOD file playback - Source: [taoG-JnkSZI]
- AdLib Jukebox for testing FM synthesis - Source: [taoG-JnkSZI]
- Check jumpers for IRQ, DMA, I/O port settings - Source: [taoG-JnkSZI]
- Use DeoxIT on edge connector before testing - Source: [taoG-JnkSZI]
- Dirty cards can cause intermittent failures - Source: [taoG-JnkSZI]
- Freezes during DMA transfer may indicate dirty connector - Source: [taoG-JnkSZI]
- Desoldering and resocketing chips can fix mysterious failures - Source: [taoG-JnkSZI]

## DIN Jack Repair

### Symptoms
- Video cuts in and out when touching/wiggling connector - Source: [Fm4aLhZtDwk]
- Flaky video, intermittent signal - Source: [Fm4aLhZtDwk]
- Lines/artifacts appearing and disappearing - Source: [Fm4aLhZtDwk]

### Diagnosis
- First try DeoxIT cleaning - may just be dirty - Source: [Fm4aLhZtDwk]
- If still flaky after cleaning: bad solder joints likely - Source: [Fm4aLhZtDwk]
- Thin traces on PCB prone to breaking - Source: [Fm4aLhZtDwk]

### Repair
- Desolder jack and inspect traces underneath - Source: [Fm4aLhZtDwk]
- Check for broken traces under solder mask - Source: [Fm4aLhZtDwk]
- May need to expose copper with Dremel and add bodge wires - Source: [Fm4aLhZtDwk]
- Add solder to bridge traces to pins - Source: [Fm4aLhZtDwk]
- Use blue tack to hold replacement jack during soldering - Source: [Fm4aLhZtDwk]
- After replacement, connection should be firm with no wiggle - Source: [Fm4aLhZtDwk]

## Keyboard Repair

### Alps SKTC Switches
- Dirt exposure can cause contact problems - debris gets inside switches - Source: [_0XGFz67DIc]
- Switches are plastic heat-staked together, making disassembly difficult - Source: [_0XGFz67DIc]
- Cleaning is possible but labor-intensive - Source: [_0XGFz67DIc]

### Alps SKCC Switches

#### Overview
- Used in Apple II, Macintosh 128/512/Plus keyboards, TRS-80 Model 3, many 1970s-80s computers - Source: [qwLa9AKsjWY]
- Also known as Alps SKCC series - Source: [qwLa9AKsjWY]
- Very common but repairable with parts swapping - Source: [qwLa9AKsjWY]
- Reference: deskthority.net/wiki/Alps_SKCC_series - Source: [qwLa9AKsjWY]

#### Disassembly
- Gray top plastic separates from white bottom housing - Source: [qwLa9AKsjWY]
- Use tweezers or X-Acto knife to unhook tabs on sides - Source: [qwLa9AKsjWY]
- Tweezers safer than blade (less risk of injury) - Source: [qwLa9AKsjWY]
- Get under gray plastic edge, slide down to release - Source: [qwLa9AKsjWY]
- Unhook both sides, then wiggle top off - Source: [qwLa9AKsjWY]
- Once practiced, becomes quick and easy - Source: [qwLa9AKsjWY]

#### Internal Components
- Slider (white plastic piece with stem for keycap) - Source: [qwLa9AKsjWY]
- Spring (sits on nub at bottom of housing) - Source: [qwLa9AKsjWY]
- Switch plate (metal contact leaves) - Source: [qwLa9AKsjWY]
- Components can be swapped between switches - Source: [qwLa9AKsjWY]

#### Common Failures
- Corroded switch plates from water/moisture damage - Source: [qwLa9AKsjWY]
- Broken slider stems - Source: [qwLa9AKsjWY]
- Missing legs (corroded off) - Source: [qwLa9AKsjWY]
- Rust on switch plate = switch won't work - Source: [qwLa9AKsjWY]

#### Repair Strategy
- Test all switches with multimeter continuity mode - Source: [qwLa9AKsjWY]
- Good switch shows 0.07 ohms or low reading when pressed - Source: [qwLa9AKsjWY]
- No continuity = bad switch - Source: [qwLa9AKsjWY]
- Harvest good switch plates from donor keyboards - Source: [qwLa9AKsjWY]
- Mac 128/512 keyboards use same SKCC switches - good donor source - Source: [qwLa9AKsjWY]

#### Parts Compatibility Notes
- Mac keyboard sliders have taller stems than some other keyboards - Source: [qwLa9AKsjWY]
- Can swap sliders to match target keyboard's keycap height - Source: [qwLa9AKsjWY]
- Springs interchangeable between all SKCC keyboards - Source: [qwLa9AKsjWY]
- Switch plates interchangeable if not corroded - Source: [qwLa9AKsjWY]
- Housings (top and bottom plastic) interchangeable - Source: [qwLa9AKsjWY]

#### Reassembly
- Put spring on slider nub - Source: [qwLa9AKsjWY]
- Insert slider with spring into bottom housing - Source: [qwLa9AKsjWY]
- Components only go together one way - Source: [qwLa9AKsjWY]
- Snap gray top back on (hooks engage automatically) - Source: [qwLa9AKsjWY]
- Test with multimeter before reinstalling - Source: [qwLa9AKsjWY]

#### DeoxIT Warning
- DeoxIT sprayed into SKCC switches does NOT work well - Source: [qwLa9AKsjWY]
- May temporarily revive switches but they fail again - Source: [qwLa9AKsjWY]
- Ultrasonic cleaner more effective for dirty switches - Source: [qwLa9AKsjWY]
- Best solution: swap parts from donor switches - Source: [qwLa9AKsjWY]

#### Desoldering from Double-Sided PCBs
- Double-sided keyboard PCBs harder to desolder than single-sided - Source: [qwLa9AKsjWY]
- Via plating connects both sides - can't just heat one side - Source: [qwLa9AKsjWY]
- Risk of ripping traces if switch not fully desoldered - Source: [qwLa9AKsjWY]
- Push IC or similar against pins from back side to pop switch out - Source: [qwLa9AKsjWY]
- If switch won't budge, still has solder on other side - Source: [qwLa9AKsjWY]
- Rust on corroded switches can wedge them into plate openings - Source: [qwLa9AKsjWY]

### SMK Switches
- Found in Apple IIe keyboards and Liberty Freedom 100 terminals - Source: [QqzmxYsK5xc]
- Same switch body but different stem/plunger lengths between models - Source: [QqzmxYsK5xc]
- Apple IIe stems are taller than Freedom 100 stems - Source: [QqzmxYsK5xc]
- Switches are disassemblable for parts swapping - Source: [QqzmxYsK5xc]
- Can swap stems, springs, housings between keyboards - Source: [QqzmxYsK5xc]
- Broken stems common problem, making keys unusable - Source: [QqzmxYsK5xc]

### Mitsumi Keyboards (C64/Atari Style)
- Springs under each key, carbon-impregnated rubber pieces press on PCB traces - Source: [Fm4aLhZtDwk]
- Very easy to service: Remove all screws, PCB comes out without removing keys - Source: [Fm4aLhZtDwk]
- Clean dust and debris with IPA - Source: [Fm4aLhZtDwk]
- For non-working keys: Can use remote control repair paint (conductive) on rubber contacts - Source: [Fm4aLhZtDwk]
- Atari 1200XL keycaps compatible with Commodore 64 keys (same cross-point mount) - Source: [Fm4aLhZtDwk]
- Springs are different between C64 and Atari but keycaps interchange - Source: [Fm4aLhZtDwk]

## Vintage Connectors and Cables

### Ribbon Cable IDC Connectors
- Clamp ribbon cable onto DIP socket footprint - Source: [4COFqpjlGuI]
- 40-pin version for CPU sockets - Source: [4COFqpjlGuI]
- Smaller versions for ROM sockets - Source: [4COFqpjlGuI]
- Very low profile (barely taller than IC) - Source: [4COFqpjlGuI]
- Used for expansion boards (TRS-80 Model 1, Apple II) - Source: [4COFqpjlGuI]
- Hard to find today - modern alternative is PCB with header - Source: [4COFqpjlGuI]
- High-quality vintage ones have gold contacts - Source: [4COFqpjlGuI]

### DB25 Ribbon Cable Connectors
- Clamp together with vise (special tool originally) - Source: [4COFqpjlGuI]
- Common method to avoid soldering individual wires - Source: [4COFqpjlGuI]
- Asian-made versions still available - Source: [4COFqpjlGuI]

### Card Edge Connectors
- Apple II style with hood/socket combination - Source: [4COFqpjlGuI]
- Same connector size as Commander X16 - Source: [4COFqpjlGuI]

## Joysticks and Controllers

### 3D Printed Joystick (HAC-2 Style)

#### Overview
- 3D printed joystick frame with commercial microswitches and handle - Source: [FnLKPVzK7bo]
- Design based on HAC-2 (Hori arcade controller) - Source: [FnLKPVzK7bo]
- Open source design by Bruno Florentino - Source: [FnLKPVzK7bo]
- GitHub: github.com/brunoflorentino/hac-2 - Source: [FnLKPVzK7bo]
- Printables: printables.com/model/1070809-hac-2-arcade-joystick - Source: [FnLKPVzK7bo]
- Designed for minimal supports (easy home printing) - Source: [FnLKPVzK7bo]

#### Parts Required
- 4x Omron D2F-01F microswitches (rated 100g) - Source: [FnLKPVzK7bo]
- Sanwa JLF handle (any brand 34mm ball top with M6 threading works) - Source: [FnLKPVzK7bo]
- Optional: Cherry MX style switches for fire buttons - Source: [FnLKPVzK7bo]
- M3 nuts and bolts for assembly - Source: [FnLKPVzK7bo]
- Total parts cost: ~$20-30 plus filament - Source: [FnLKPVzK7bo]

#### Build Notes
- Switch pressure determines feel (100g recommended) - Source: [FnLKPVzK7bo]
- Can use heavier switches (200g) for stiffer response - Source: [FnLKPVzK7bo]
- Actuator length affects engage/disengage point - Source: [FnLKPVzK7bo]
- Requires filing/adjustment if parts don't fit precisely - Source: [FnLKPVzK7bo]
- Red filament looks authentic to arcade aesthetic - Source: [FnLKPVzK7bo]

#### Wiring
- Directly wire to DE9 connector for Atari/Commodore use - Source: [FnLKPVzK7bo]
- DE9 pinout: Up=1, Down=2, Left=3, Right=4, Fire=6, Ground=8 - Source: [FnLKPVzK7bo]
- Standard Atari pinout compatible with C64, Amiga, Atari ST, etc. - Source: [FnLKPVzK7bo]

### Nichicon VZ Capacitor Series (Known Problem)
- Nichicon VZ series capacitors from 1990s are notorious leakers - Source: [FnLKPVzK7bo]
- Found in many ISA sound cards, motherboards of the era - Source: [FnLKPVzK7bo]
- Brown/tan cylindrical caps with blue stripe - Source: [FnLKPVzK7bo]
- Leak corrosive electrolyte that damages PCB traces - Source: [FnLKPVzK7bo]
- Replace ALL VZ series caps preemptively when found - Source: [FnLKPVzK7bo]
- Other Nichicon series (non-VZ) from same era often fine - Source: [FnLKPVzK7bo]
