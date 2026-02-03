# Western Digital

## Models
| Model | Category | Videos Referenced |
|-------|----------|-------------------|
| WD1002-WAH | MFM Controller (16-bit ISA) | [bgW5tpyJljM] |
| WD1003-WAH | MFM Controller (16-bit ISA) | [bgW5tpyJljM] |
| WD10-IFC Filecard | Hard Card (8-bit ISA) | [cXbDSudlSTQ] |
| MFM Controller (Gold Board) | MFM Controller | [CpQ2j2J6wL0] |

## Platform-Specific Knowledge

### MFM Controllers

#### Gold Board Controller
- High quality Western Digital MFM controller - Source: [CpQ2j2J6wL0]
- Reliable performance with various MFM drives - Source: [CpQ2j2J6wL0]
- Significantly better than some other brands (e.g., NDC 5525) - Source: [CpQ2j2J6wL0]

#### Controller Compatibility
- 16-bit ISA MFM controllers generally interchangeable - Source: [bgW5tpyJljM]
- Drive formatted with one controller readable by another - Source: [bgW5tpyJljM]
- Different controllers may need different interleave settings - Source: [bgW5tpyJljM]

#### NDC 5525 Comparison
- Alternative 16-bit MFM controller - Source: [CpQ2j2J6wL0]
- Some units have severe performance problems - Source: [CpQ2j2J6wL0]
- Can read at only ~10 KB/sec vs ~300 KB/sec on WD controller - Source: [CpQ2j2J6wL0]
- May appear to "work" but with unacceptable speeds - Source: [CpQ2j2J6wL0]
- No visible damage; just internally defective - Source: [CpQ2j2J6wL0]
- Controllers do go bad in weird, unpredictable ways - Source: [CpQ2j2J6wL0]

### WD10-IFC Filecard (Hard Card)
- ISA 8-bit hard card with integrated hard drive - Source: [cXbDSudlSTQ]
- Features metal cover over drive mechanism - Source: [cXbDSudlSTQ]
- Contains unusual JVC JD3812M hard drive - Source: [cXbDSudlSTQ]
- Has custom interface (not standard MFM connectors on drive) - Source: [cXbDSudlSTQ]
- Has secondary connector for potential expansion or second drive - Source: [cXbDSudlSTQ]
- Has ISA bus pass-through expansion connector - Source: [cXbDSudlSTQ]
- Made in USA by Western Digital Corporation, Irvine California - Source: [cXbDSudlSTQ]

#### Troubleshooting Controllers
- If drive appears slow, try different controller before blaming drive - Source: [CpQ2j2J6wL0]
- Always test with known-good controller when possible - Source: [CpQ2j2J6wL0]
- Check jumpers for base I/O settings - Source: [CpQ2j2J6wL0]
- No performance jumpers on these controllers - Source: [CpQ2j2J6wL0]
