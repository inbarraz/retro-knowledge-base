# ASUS

## Models
| Model | Category | Videos Referenced |
|-------|----------|-------------------|
| PVI-486SP3 | Motherboard | [Li2xFBGbzZQ] |

## Platform-Specific Knowledge

### ASUS PVI-486SP3 Motherboard

#### Overview
- Socket 3 486 motherboard - Source: [Li2xFBGbzZQ]
- Triple bus design: PCI, VLB (VESA Local Bus), and ISA slots - Source: [Li2xFBGbzZQ]
- Uncommon combination of all three bus types - Source: [Li2xFBGbzZQ]
- Uses SiS 85C496 and 85C497 chipset - Source: [Li2xFBGbzZQ]

#### CPU Support
- Socket 3 (3.3V or 5V) for 486 processors - Source: [Li2xFBGbzZQ]
- Supports 486DX, DX2, DX4 processors - Source: [Li2xFBGbzZQ]
- Also supports AMD 5x86 and Cyrix 5x86 CPUs - Source: [Li2xFBGbzZQ]
- Jumpers configure voltage and clock multiplier - Source: [Li2xFBGbzZQ]

#### Cache Memory
- 512KB L2 cache capacity - Source: [Li2xFBGbzZQ]
- Uses 32Kx8 SRAM chips (eight chips total) - Source: [Li2xFBGbzZQ]
- Cache significantly improves performance - Source: [Li2xFBGbzZQ]
- Cache tag RAM chip near main cache chips - Source: [Li2xFBGbzZQ]

#### RAM Compatibility Issues

##### EDO vs Fast Page RAM
- CRITICAL: Only Fast Page (FP) RAM works reliably - Source: [Li2xFBGbzZQ]
- EDO RAM causes POST failures despite BIOS claiming EDO support - Source: [Li2xFBGbzZQ]
- Symptoms with EDO: Hangs during memory count, random POST failures - Source: [Li2xFBGbzZQ]
- Mix of EDO and FP may cause intermittent issues - Source: [Li2xFBGbzZQ]

##### RAM Identification Tips
- Check chip markings for "-60" (60ns) timing - Source: [Li2xFBGbzZQ]
- EDO chips may have "EDO" in part number or manufacturer code - Source: [Li2xFBGbzZQ]
- When in doubt, test SIMMs individually - Source: [Li2xFBGbzZQ]
- 72-pin SIMMs required for this board - Source: [Li2xFBGbzZQ]

##### SIMM Banks
- Four SIMM sockets - Source: [Li2xFBGbzZQ]
- 32-bit data path requires paired installation - Source: [Li2xFBGbzZQ]
- Can use 4MB, 8MB, 16MB, or 32MB SIMMs - Source: [Li2xFBGbzZQ]

#### VLB Slot Notes
- VLB slots share electrical signals with ISA - Source: [Li2xFBGbzZQ]
- VLB cards plug into both ISA and VLB connectors - Source: [Li2xFBGbzZQ]
- Not all VLB cards work in all VLB slots (signal length issues) - Source: [Li2xFBGbzZQ]
- Try different VLB slot if card doesn't work - Source: [Li2xFBGbzZQ]

#### ISA Bus Speed Observation
- ISA bus transfers slower on 486 than expected - Source: [Li2xFBGbzZQ]
- Speed600 benchmark showed ~2600 bytes/ms for ISA - Source: [Li2xFBGbzZQ]
- 386SX boards often show ~5600 bytes/ms for same ISA card - Source: [Li2xFBGbzZQ]
- May be chipset limitation or ISA clock divider setting - Source: [Li2xFBGbzZQ]

#### Dallas RTC Chip
- Uses Dallas DS1287 or DS1287A RTC - Source: [Li2xFBGbzZQ]
- Dead Dallas chip = no clock, settings reset on power loss - Source: [Li2xFBGbzZQ]
- Can replace with NecroWare Dallas replacement module - Source: [Li2xFBGbzZQ]
- Dallas failure doesn't prevent board from working - Source: [Li2xFBGbzZQ]

#### BIOS
- Award BIOS - Source: [Li2xFBGbzZQ]
- Settings for cache, shadow RAM, ISA timing - Source: [Li2xFBGbzZQ]
- Can adjust wait states for ISA if compatibility issues - Source: [Li2xFBGbzZQ]

## General 486 Motherboard Notes

### ISA vs VLB vs PCI Speed
- PCI fastest for video cards (~8000+ bytes/ms in Speed600) - Source: [Li2xFBGbzZQ]
- VLB comparable to PCI for video (~7000-8000 bytes/ms) - Source: [Li2xFBGbzZQ]
- ISA much slower (~2000-3000 bytes/ms) - Source: [Li2xFBGbzZQ]
- Use PCI or VLB video card for best DOS game performance - Source: [Li2xFBGbzZQ]

### Speed600 Benchmark
- Tests video memory transfer rate - Source: [Li2xFBGbzZQ]
- Results in bytes per millisecond - Source: [Li2xFBGbzZQ]
- Good for comparing different video cards/buses - Source: [Li2xFBGbzZQ]
- Doesn't measure CPU speed, only video path - Source: [Li2xFBGbzZQ]

### VidSpeed Utility
- Similar to Speed600 but different test methodology - Source: [Li2xFBGbzZQ]
- Tests actual scrolling/drawing performance - Source: [Li2xFBGbzZQ]
- Useful for comparing real-world video performance - Source: [Li2xFBGbzZQ]
