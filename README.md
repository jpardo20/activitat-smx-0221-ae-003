# AE-003 · Fitxa tècnica de la **torre** (sense SO)
**M0221 – Muntatge i manteniment d'equips (1r SMX)**

> **Important:** Només la **torre**. **Sense** monitor, teclat, ratolí ni **sistema operatiu** indicat enlloc (ni text ni captures).

## Objectius didàctics
- Identificar amb precisió **components i especificacions** d’un PC de sobretaula (torre).
- Verificar **compatibilitats i recursos**: ranures, ports, alimentació, capacitats.
- Documentar **estat i manteniment** de la màquina.
- Comunicar en format **fitxa comercial/tècnica** clara i reutilitzable.

## Lliurables (3 elements)
1. **Fitxa tècnica** de la torre en **MD o HTML** (vegeu `/templates`).
2. **Fotografies** (5–8): frontal, posterior, interior, etiqueta de la PSU, detalls de ports/ranures. *(Sense números de sèrie ni MAC visibles.)*
> **Privacitat:** No inclogueu números de sèrie, adreces MAC, claus de producte ni informació de l’SO. Tapeu o retalleu si cal.

## Checklist (només torre)
- [ ] Caixa: format, dimensions, baies 3.5"/2.5", (opc.) pes, filtres.
- [ ] Placa base: model, xipset, socket, **BIOS/UEFI v.**, M.2 (nº i estat), SATA (usats/lliures), format (ATX/mATX/ITX).
- [ ] CPU: model, nuclis/fils, GHz base (opc. boost), TDP.
- [ ] RAM: capacitat total, tipus (DDR3/4/5), velocitat, bancs ocupats/lliures, màx. suportat.
- [ ] Emmagatzematge: llista de discos (NVMe/SATA/HDD) i capacitat; (opc.) estat SMART (OK/Warning).
- [ ] Gràfics: integrada o GPU dedicada (model), memòria; sortides (HDMI/DP/DVI).
- [ ] Alimentació (PSU): marca/model, **potència (W)**, certificació (80+), connectors disponibles (PCIe/CPU/ATX).
- [ ] Refrigeració: cooler CPU, ventiladors (nº i mida), flux d’aire.
- [ ] Connectivitat: USB (nº per tipus), àudio, Ethernet (1G/2.5G), Wi‑Fi/Bluetooth si n’hi ha.
- [ ] Expansió: PCIe ocupats/lliures, headers (USB, ARGB, fan…).
- [ ] Manteniment: neteja recent, cablejat, pasta tèrmica, peces canviades i data.
- [ ] **Sense cap menció a l’SO.**

## Estructura del repo
```
activitat-smx-0221-ae-003/
├─ README.md
├─ templates/
│  ├─ plantilla-fitxa-torre.md
│  └─ plantilla-fitxa-torre.html
├─ docs/         # Versió HTML per publicar (GitHub Pages)
└─ lliurament/
   └─ instruccions-lliurament.md
```

## Bones pràctiques
- Llenguatge clar: especificació → benefici (“NVMe 512 GB → arrencada/accés molt ràpid”).  
- Taula resum al principi + detalls per seccions.  
- Fotos nítides, fons uniforme, ports visibles i interior net.  
- No confongueu **capacitat instal·lada** vs. **adreçable** (p. ex. RAM).

---

© 2025 · Llicència **CC BY-SA 4.0** (atribució i compartició en les mateixes condicions).