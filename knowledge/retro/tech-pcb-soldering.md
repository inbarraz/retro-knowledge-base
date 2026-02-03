# PCB Repair and Soldering Techniques

> Part of the retro knowledge base. See also: tech-*.md files for other categories.

## Contents
- [PCB Crack Repair](#pcb-crack-repair)
- [Corrosion Repair](#corrosion-repair)
- [SMD Capacitor Removal](#smd-capacitor-removal)
- [Wire Wrapping](#wire-wrapping)
- [ISA Slot Replacement](#isa-slot-replacement)
- [PCB Repair Supplies](#pcb-repair-supplies)
- [Soldering Flux Types](#soldering-flux-types)

## PCB Crack Repair

### Assessment
- Check all traces crossing crack for continuity - Source: [8cLNKB_sajA]
- Traces may look intact but be broken underneath - Source: [8cLNKB_sajA]
- Anticipate where cracks might grow and bridge preventatively - Source: [8cLNKB_sajA]

### Repair Method
- Use thick wire for high-current traces (power, horizontal drive) - Source: [8cLNKB_sajA]
- Thinner wire acceptable for signal traces - Source: [8cLNKB_sajA]
- Small metal strips can bridge multiple adjacent pins - Source: [8cLNKB_sajA]
- Watch for isolation gaps between pins when bridging - Source: [8cLNKB_sajA]
- Dig under solder mask to verify trace endpoints - Source: [8cLNKB_sajA]

### Stabilization
- Apply hot glue to secure bodge wires after testing - Source: [8cLNKB_sajA]
- Consider JB Weld or epoxy for structural reinforcement - Source: [8cLNKB_sajA]
- Not a permanent fix - further impact may cause more cracks - Source: [8cLNKB_sajA]

## Corrosion Repair

### Naval Jelly (Loctite Rust Dissolver)
- Paint-on jelly consistency stays in place unlike liquid cleaners - Source: [0WMTYZ60OvE]
- Let sit 5-10 minutes, foams up as it works - Source: [0WMTYZ60OvE]
- Works very quickly on green battery corrosion - Source: [0WMTYZ60OvE]
- MUST wash thoroughly with soap and water after treatment - residue will continue eating metal - Source: [0WMTYZ60OvE]
- Do NOT use on aluminum, chrome, or stainless steel - Source: [0WMTYZ60OvE]
- Can get into slot connectors easily due to thick gel consistency - Source: [0WMTYZ60OvE]
- Works well for battery leak corrosion recovery - Source: [0WMTYZ60OvE]
- For heavy corrosion: Let sit ~20 minutes, may need multiple passes - Source: [36NPrsEcNww]
- NiCad battery leakage is basic - naval jelly (phosphoric acid) neutralizes it - Source: [36NPrsEcNww]
- Use cheap disposable paintbrush to apply (dollar store bags of 10-20) - Source: [36NPrsEcNww]

### Vinegar Alternative
- Milder than naval jelly, takes longer but less aggressive - Source: [36NPrsEcNww]
- Vinegar soak method: Wrap PCB in plastic wrap, pour vinegar over it - Source: [36NPrsEcNww]
- Good for heavily corroded boards where naval jelly would be too much - Source: [36NPrsEcNww]
- Citric acid also works as alternative - Source: [36NPrsEcNww]

### Post-Corrosion Protection
- Clear nail polish: Paint over exposed copper areas to prevent future oxidation - Source: [0WMTYZ60OvE]
- Do NOT put nail polish on edge connector contacts - must remain conductive - Source: [0WMTYZ60OvE]
- DeoxIT provides temporary oil coating on contacts - Source: [0WMTYZ60OvE]
- Can tin exposed copper with solder, but may shed material into slots - Source: [0WMTYZ60OvE]

### Evapo-Rust Treatment (Full Board Submersion)
- Evapo-Rust is non-toxic chelating rust remover, safe for electronics - Source: [cuBAq110pr8]
- Can submerge entire motherboard/PCB to remove rust and corrosion - Source: [cuBAq110pr8]
- Works on RF shields, chassis components, and exposed metal parts - Source: [cuBAq110pr8]
- Does not damage ICs, capacitors, resistors, or PCB substrate - Source: [cuBAq110pr8]
- Rinse thoroughly with clean water after treatment - Source: [cuBAq110pr8]
- CRITICAL: Allow complete drying (days) before attempting power-on - Source: [cuBAq110pr8]
- Trapped moisture under chips or in connectors can cause shorts - Source: [cuBAq110pr8]
- Follow up with nail polish protection on vulnerable cleaned areas - Source: [cuBAq110pr8]

### NiCad Battery Corrosion Cleanup (Comprehensive)

#### Tools
- Dremel with jewelry polishing rubber tips (abrasive) - Source: [ckTx8G3JImI]
- Engraving tool with fine bit for precision - Source: [ckTx8G3JImI]
- IPA and brush for cleaning debris during work - Source: [ckTx8G3JImI]

#### Inspection
- Look for bubbles/discoloration in traces = corrosion underneath - Source: [ckTx8G3JImI]
- Check vias near battery for hidden corrosion - Source: [ckTx8G3JImI]
- Flip board and check traces on bottom side - Source: [ckTx8G3JImI]
- Corrosion may spread along traces away from battery - Source: [ckTx8G3JImI]

#### Trace Cleaning
- Use rubber tip to remove solder mask and expose corroded copper - Source: [ckTx8G3JImI]
- IPA spray makes progress visible between passes - Source: [ckTx8G3JImI]
- Rubber tips wear out quickly - buy in bulk - Source: [ckTx8G3JImI]

#### Trace Repair
- Use resistor leg wire to bridge corroded/broken sections - Source: [ckTx8G3JImI]
- Flux helps solder adhere to exposed copper - Source: [ckTx8G3JImI]
- Reinforce obviously weak traces preventatively - Source: [ckTx8G3JImI]

#### CR2032 Battery Modification
- Identify and remove diode in charging path from 5V to battery - Source: [ckTx8G3JImI]
- Verify 5V no longer present at battery terminals when powered - Source: [ckTx8G3JImI]
- Multiple diodes in series may need removing when using 3V CR2032 - Source: [ckTx8G3JImI]
- Dallas chip drop-in replacement or Necroware clock module alternatives - Source: [ckTx8G3JImI]

### Dallas RTC Chip Replacement

#### Overview
- Dallas DS1287/DS1287A integrated RTC chips have internal battery that dies - Source: [LODGfYNckMc], [HtrAvQGuXTw]
- Internal battery cannot be replaced in original chip design - Source: [LODGfYNckMc]
- Dead Dallas chip = no time keeping, CMOS settings reset on power loss - Source: [HtrAvQGuXTw]
- Dallas chips do NOT leak and corrode like NiCad batteries - Source: [HtrAvQGuXTw]
- Dallas failure is benign - board still functions, just loses settings - Source: [HtrAvQGuXTw]

#### NecroWare Dallas Replacement Module (NWX287)
- Modern drop-in replacement for Dallas DS1287/DS1287A - Source: [LODGfYNckMc], [m1P5-VYB9U0]
- Uses CR2032 battery holder (user-replaceable battery) - Source: [LODGfYNckMc]
- Same pinout as original Dallas chip - Source: [LODGfYNckMc]
- GitHub: github.com/necroware/nwX287 - Source: [m1P5-VYB9U0]
- Can be ordered pre-assembled or built from PCB + components - Source: [LODGfYNckMc]
- Works in IBM AT, 286/386/486 motherboards with Dallas chips - Source: [m1P5-VYB9U0]

#### Motorola Mode for Non-Intel Systems
- Some systems (BBC Master, etc.) use Motorola chip select conventions - Source: [m1P5-VYB9U0]
- Dallas RTC originally available in Intel or Motorola versions - Source: [m1P5-VYB9U0]
- NecroWare module can be configured for Motorola mode - Source: [m1P5-VYB9U0]
- Requires adding resistor between specific pins on module - Source: [m1P5-VYB9U0]
- Check system documentation for which mode is required - Source: [m1P5-VYB9U0]
- Wrong mode = RTC not recognized or incorrect data - Source: [m1P5-VYB9U0]

#### Installation
- Remove original Dallas chip from socket (may be soldered) - Source: [LODGfYNckMc]
- If soldered: Desolder carefully or use chip extraction tool - Source: [LODGfYNckMc]
- Install replacement module in same socket - Source: [LODGfYNckMc]
- Insert CR2032 battery - Source: [LODGfYNckMc]
- Verify CMOS settings are saved across power cycles - Source: [LODGfYNckMc]

#### Battery Damage Assessment (Mac IIfx, etc.)
- Some battery damage too extensive to repair economically - Source: [m1P5-VYB9U0]
- Signs of unrecoverable damage: eaten-through PCB layers, destroyed vias - Source: [m1P5-VYB9U0]
- If corrosion is under BGA or QFP chips, repair very difficult - Source: [m1P5-VYB9U0]
- Better to salvage working chips (CPU, FPU, RAM) for other repairs - Source: [m1P5-VYB9U0]
- Don't waste hours on boards that are fundamentally destroyed - Source: [m1P5-VYB9U0]

#### Dallas vs NiCad Barrel Battery
- Dallas chip failure: No corrosion, board still usable - Source: [HtrAvQGuXTw]
- NiCad barrel battery: Leaks, corrodes traces, can destroy board - Source: [HtrAvQGuXTw]
- Boards with Dallas only (no barrel) often survive decades - Source: [HtrAvQGuXTw]
- Always check for and remove NiCad batteries; Dallas can stay - Source: [HtrAvQGuXTw]

## MLCC Ceramic Capacitor DC Bias Derating

### Overview
- Multi-layer ceramic capacitors (MLCC) lose capacitance at operating voltage - Source: [rpVAg6hG__Y]
- Unlike electrolytic caps, MLCC effective capacitance drops significantly with DC bias - Source: [rpVAg6hG__Y]
- Must consider this when using MLCC to replace electrolytic caps - Source: [rpVAg6hG__Y]

### Derating Examples (Typical X5R/X7R Ceramic)
- 47µF cap at 2V: Full rated capacitance - Source: [rpVAg6hG__Y]
- 47µF cap at 5V: ~30% loss = actual ~32µF - Source: [rpVAg6hG__Y]
- 47µF cap at 12V: ~50-70% loss - Source: [rpVAg6hG__Y]
- 16V rated cap at 16V: Up to 70% capacitance loss - Source: [rpVAg6hG__Y]

### Practical Application for Recapping
- When replacing 10µF electrolytics with MLCC, use 22µF to compensate - Source: [rpVAg6hG__Y]
- 22µF MLCC at 5V will provide approximately 15-17µF effective - Source: [rpVAg6hG__Y]
- Check MLCC data sheets for DC bias curves (look for "DC bias characteristics") - Source: [rpVAg6hG__Y]
- Aluminum electrolytics do not exhibit this derating behavior - Source: [rpVAg6hG__Y]

### When This Matters
- 5V logic circuits: 30% derating typical - Source: [rpVAg6hG__Y]
- 12V circuits (floppy drives, etc.): More significant derating - Source: [rpVAg6hG__Y]
- Better to slightly oversize MLCC than undersize - Source: [rpVAg6hG__Y]
- If machine misbehaves after MLCC recap, try higher values - Source: [rpVAg6hG__Y]

## SMD Capacitor Removal

### Twist Method for Electrolytics
- Use fine-tip pliers to grip SMD capacitor body - Source: [PecWdDkabFc]
- Twist cap gently while applying slight upward pressure - Source: [PecWdDkabFc]
- Cap detaches from pads cleanly in most cases - Source: [PecWdDkabFc]
- Faster than desoldering with iron for many caps - Source: [PecWdDkabFc]
- Works because solder joints become brittle after decades - Source: [PecWdDkabFc]
- If cap resists, heat with iron then twist - Source: [PecWdDkabFc]
- Works well on Macs and other systems with SMD electrolytics - Source: [PecWdDkabFc]

### Pad Cleanup After Removal
- After twisting off cap, residual solder remains on pads - Source: [PecWdDkabFc]
- Apply fresh solder to each pad then remove with solder wick - Source: [PecWdDkabFc]
- Clean pads with IPA to remove flux residue - Source: [PecWdDkabFc]
- Inspect pads for damage before installing new caps - Source: [PecWdDkabFc]
- Lifted pads may need repair with copper tape or bodge wires - Source: [PecWdDkabFc]

### Installing Replacement Caps
- SMD electrolytics have polarity marking (stripe = negative usually) - Source: [PecWdDkabFc]
- Apply solder to one pad, tack cap in place with tweezers - Source: [PecWdDkabFc]
- Solder second terminal, then reflow first for alignment - Source: [PecWdDkabFc]
- Use low-profile or same-size caps as originals when possible - Source: [PecWdDkabFc]

## Wire Wrapping

### Overview
- Point-to-point wiring technique using solid core wire wound tightly around posts - Source: [HqgpgZrscCA]
- Common construction method for prototypes and small production runs in 1970s-1980s - Source: [HqgpgZrscCA]
- Still useful for repairs, modifications, and one-off projects - Source: [HqgpgZrscCA]

### Tools

#### Wire Wrapping Tool
- Hand tool that wraps wire around square posts - Source: [HqgpgZrscCA]
- Has two holes: center hole for post, offset hole for wire - Source: [HqgpgZrscCA]
- Rotating tool wraps wire around post in tight helical coil - Source: [HqgpgZrscCA]
- Spring-loaded versions available for faster operation - Source: [HqgpgZrscCA]
- Quality tools from OK Industries, Vector, Radio Shack - Source: [HqgpgZrscCA]

#### Wire Unwrapping Tool
- Separate tool for removing wire wrap connections - Source: [HqgpgZrscCA]
- Tubular tool that fits over post - Source: [HqgpgZrscCA]
- Rotating unwraps existing connection - Source: [HqgpgZrscCA]
- Essential for rework or corrections - Source: [HqgpgZrscCA]

#### Wire
- 30 AWG (0.25mm) solid core wire standard for wire wrap - Source: [HqgpgZrscCA]
- Kynar insulation common (blue, white, yellow, red available) - Source: [HqgpgZrscCA]
- Pre-stripped wire available in various lengths - Source: [HqgpgZrscCA]
- Can strip standard wire with wire wrap stripper tool - Source: [HqgpgZrscCA]

### Technique

#### Proper Wire Wrap Connection
- Strip about 1" of insulation from wire end - Source: [HqgpgZrscCA]
- Insert wire through offset hole in tool - Source: [HqgpgZrscCA]
- Place tool over post (post goes in center hole) - Source: [HqgpgZrscCA]
- Rotate tool to wrap wire around post - Source: [HqgpgZrscCA]
- Should get 6-8 tight turns minimum - Source: [HqgpgZrscCA]
- Some turns should include insulation (modified wrap) for strain relief - Source: [HqgpgZrscCA]

#### Connection Quality
- Gas-tight connection without solder - Source: [HqgpgZrscCA]
- Sharp corners of square post bite into wire - Source: [HqgpgZrscCA]
- Very reliable when done properly - Source: [HqgpgZrscCA]
- Connections remain good for decades - Source: [HqgpgZrscCA]
- Can be soldered for extra security if needed - Source: [HqgpgZrscCA]

### Applications

#### Prototype Construction
- Faster than PCB layout for one-offs - Source: [HqgpgZrscCA]
- Easy to modify/correct mistakes - Source: [HqgpgZrscCA]
- Wire wrap sockets hold ICs, provide posts for connections - Source: [HqgpgZrscCA]
- Wire wrap boards provide grid of posts for discrete components - Source: [HqgpgZrscCA]

#### Vintage Computer Repair
- Adding bodge wires to fix broken traces - Source: [HqgpgZrscCA]
- Connecting mod boards to existing circuits - Source: [HqgpgZrscCA]
- Cleaner than soldering loose wires to IC pins - Source: [HqgpgZrscCA]
- Wire wrap sockets available for retrofitting - Source: [HqgpgZrscCA]

### Modern Availability
- Wire wrap tools still available (Amazon, electronics suppliers) - Source: [HqgpgZrscCA]
- Wire wrap wire still manufactured - Source: [HqgpgZrscCA]
- Wire wrap sockets becoming harder to find (DIP sockets with long pins) - Source: [HqgpgZrscCA]
- Vintage NOS (new old stock) tools often higher quality than new production - Source: [HqgpgZrscCA]

## ISA Slot Replacement

### Overview
- Complete replacement of damaged/corroded ISA slot connectors - Source: [hStIrdagIJs]
- Required when contacts are pitted, corroded, or physically damaged - Source: [hStIrdagIJs]
- Many pins (62-pin for 8-bit, 98-pin for 16-bit ISA) makes this challenging - Source: [hStIrdagIJs]

### When to Replace vs Clean
- Light corrosion: Clean with fiberglass brush or Dremel polishing wheel - Source: [hStIrdagIJs]
- Heavy pitting/corrosion: Cleaning won't restore reliable contact, replace - Source: [hStIrdagIJs]
- Missing/broken plastic: Replace the slot - Source: [hStIrdagIJs]
- Intermittent card contact after cleaning: Replace the slot - Source: [hStIrdagIJs]

### Tools Required
- Hot air rework station (capable of 350°C / 660°F) - Source: [hStIrdagIJs]
- Desoldering iron (Hakko FR-301 or similar) - Source: [hStIrdagIJs]
- Both tools needed together - neither alone is sufficient - Source: [hStIrdagIJs]
- Replacement ISA slot connectors (available on AliExpress, eBay) - Source: [hStIrdagIJs]
- Flux (gel flux recommended) - Source: [hStIrdagIJs]
- Solder wick for cleanup - Source: [hStIrdagIJs]

### Removal Technique

#### Hot Air + Desoldering Iron Method
- Apply flux to all pins on both sides of slot - Source: [hStIrdagIJs]
- Set hot air station to 350°C with medium airflow - Source: [hStIrdagIJs]
- Set desoldering iron to 350°C - Source: [hStIrdagIJs]
- Heat one side of slot with hot air while working other side with desolder iron - Source: [hStIrdagIJs]
- Hot air preheats/keeps solder molten while desolder iron removes it - Source: [hStIrdagIJs]
- Work quickly to avoid overheating PCB or nearby components - Source: [hStIrdagIJs]

#### Sequence
1. Apply flux liberally to all pins - Source: [hStIrdagIJs]
2. Heat from bottom side with hot air - Source: [hStIrdagIJs]
3. Work along row with desoldering iron from top - Source: [hStIrdagIJs]
4. Repeat for all rows of pins - Source: [hStIrdagIJs]
5. Gently rock slot side-to-side while heating to check if free - Source: [hStIrdagIJs]
6. Continue desoldering until slot lifts out cleanly - Source: [hStIrdagIJs]

#### Common Issues
- Old lead solder melts easily, lead-free is harder - Source: [hStIrdagIJs]
- Some pins may wick solder back from traces - re-desolder - Source: [hStIrdagIJs]
- Don't force - if slot won't come out, more pins still attached - Source: [hStIrdagIJs]
- PCB can delaminate if overheated too long - keep moving - Source: [hStIrdagIJs]

### Installation

#### Hole Cleanup
- Inspect all holes for remaining solder - Source: [hStIrdagIJs]
- Use desoldering iron to clear blocked holes - Source: [hStIrdagIJs]
- Solder wick for stubborn holes - Source: [hStIrdagIJs]
- All holes must be clear before inserting new slot - Source: [hStIrdagIJs]

#### Fitting New Slot
- Test fit new slot in holes before soldering - Source: [hStIrdagIJs]
- All pins should go through without forcing - Source: [hStIrdagIJs]
- May need to straighten bent pins on new connector - Source: [hStIrdagIJs]
- Seat connector fully flush against PCB - Source: [hStIrdagIJs]

#### Soldering New Slot
- Tack two corner pins first to hold in place - Source: [hStIrdagIJs]
- Verify connector is square and fully seated - Source: [hStIrdagIJs]
- Solder all remaining pins - Source: [hStIrdagIJs]
- Touch up any cold joints - Source: [hStIrdagIJs]
- Inspect for bridges between adjacent pins - Source: [hStIrdagIJs]
- Clean flux residue with IPA - Source: [hStIrdagIJs]

### Testing After Replacement
- Visual inspection for cold joints, bridges - Source: [hStIrdagIJs]
- Insert ISA card and verify firm seating - Source: [hStIrdagIJs]
- Test with simple card first (POST card, serial card) - Source: [hStIrdagIJs]
- Check for proper contact before testing expensive cards - Source: [hStIrdagIJs]

### Replacement Connector Sources
- AliExpress: Search "ISA slot connector" - Source: [hStIrdagIJs]
- eBay: Both new and salvaged available - Source: [hStIrdagIJs]
- Salvage from dead motherboards (if contacts still good) - Source: [hStIrdagIJs]
- Quality varies - inspect new connectors before use - Source: [hStIrdagIJs]

## PCB Repair Supplies

### Conductive Copper Tape
- Self-adhesive copper tape for PCB trace repair - Source: [ND0BH5ePRIE]
- Conductive adhesive allows electrical continuity - Source: [ND0BH5ePRIE]
- Cut to size to bridge broken traces - Source: [ND0BH5ePRIE]
- Can be soldered to for permanent connection - Source: [ND0BH5ePRIE]
- Useful for repairing lifted pads and corroded traces - Source: [ND0BH5ePRIE]
- Available in various widths from electronics suppliers - Source: [ND0BH5ePRIE]

### Silicone Heat-Resistant Mat
- Flexible work surface for soldering - Source: [ND0BH5ePRIE]
- Protects workbench from heat and flux - Source: [ND0BH5ePRIE]
- Organizer sections for small parts - Source: [ND0BH5ePRIE]
- Resists soldering iron temperatures - Source: [ND0BH5ePRIE]
- Easy to clean flux and solder residue - Source: [ND0BH5ePRIE]

## Edge Connector Tinning

### Corrosion Recovery via Tinning
- For badly corroded edge connector contacts that cleaning alone can't restore - Source: [u309Zbn9o10]
- Clean card edge first with IPA and magic eraser to remove loose oxidation - Source: [u309Zbn9o10]
- Apply rosin flux to corroded contacts - Source: [u309Zbn9o10]
- Apply thin layer of solder to each contact (tinning) - Source: [u309Zbn9o10]
- Use Chemtronics solder wick to remove excess solder - Source: [u309Zbn9o10]
- Result: Smooth, conductive surface protected from future corrosion - Source: [u309Zbn9o10]
- Tinning creates corrosion barrier on otherwise exposed copper - Source: [u309Zbn9o10]

### Protecting Non-Contact Areas
- Clear nail polish or lacquer on traces/vias near edge connector - Source: [u309Zbn9o10]
- Do NOT apply lacquer to actual contact fingers (need conductivity) - Source: [u309Zbn9o10]
- Protects cleaned copper from re-oxidizing - Source: [u309Zbn9o10]

## Soldering Flux Types

### Amtech Aerospace Grade Flux
- Viscous tacky flux used by professional repair technicians - Source: [NHz1e1Wu1iI]
- "What Louis Rossman uses" - reference for board repair community - Source: [NHz1e1Wu1iI]
- Much thicker consistency than MG Chemicals rosin flux - Source: [NHz1e1Wu1iI]
- Stays in place during heating - doesn't run off - Source: [NHz1e1Wu1iI]
- Better for BGA and fine-pitch SMD work - Source: [NHz1e1Wu1iI]
- More expensive but lasts longer due to less waste - Source: [NHz1e1Wu1iI]
- NC-559-V2-TF is common variant - Source: [NHz1e1Wu1iI]

### Solder Wick Quality
- Cheap solder wick performs very poorly compared to quality brands - Source: [rpVAg6hG__Y]
- MG Chemicals: Reliable quality, commonly available - Source: [rpVAg6hG__Y]
- Chip Quik: High quality, cleans pads very well with minimal residue - Source: [rpVAg6hG__Y]
- Quality wick makes quick work of pad cleanup after cap removal - Source: [rpVAg6hG__Y]
- Good wick leaves shiny, clean pads ready for new components - Source: [rpVAg6hG__Y]
- Stick to quality brands - the difference is dramatic - Source: [rpVAg6hG__Y]

### Rosin Flux for SMD Work
- Rosin flux applied to pads before component placement helps adhesion - Source: [rpVAg6hG__Y]
- Flux is sticky - holds components in place during soldering - Source: [rpVAg6hG__Y]
- Apply dot of flux between each cap location - Source: [rpVAg6hG__Y]
- Solder on iron tip mixes with flux for easy tacking - Source: [rpVAg6hG__Y]
- Clean flux residue after soldering with IPA and cotton bud - Source: [rpVAg6hG__Y]
- Flux residue is not harmful but looks unsightly - Source: [rpVAg6hG__Y]

### SIMM Slot Protection During Recapping
- Cover SIMM/RAM slots with tape before soldering nearby - Source: [rpVAg6hG__Y]
- Solder blobs in memory slots cause nightmare troubleshooting - Source: [rpVAg6hG__Y]
- Small precaution saves significant problems later - Source: [rpVAg6hG__Y]
