# Aircraft Technical Documentation Impact & Configuration Manager

## Overview

This educational project simulates how aircraft maintenance documentation 
(AMM, IPC, TSM) is assessed and updated when aircraft design changes occur.

## Features

- ATA chapter classification
- Revision tracking
- Configuration effectivity
- Compliance traceability
- Impact assessment workflow

## Project Structure

- models.py → Manual data model and revision control
- impact_engine.py → ATA-based impact detection logic
- compliance.py → ICA and configuration validation simulation
- sample_data.py → Mock AMM/IPC/TSM dataset
- main.py → CLI workflow

## How to Run

```bash
python main.py
```

Follow CLI prompts to submit a design change and observe documentation updates.

## Educational Purpose

This is a simplified academic simulation inspired by real aircraft technical 
data lifecycle processes. It does not represent actual Airbus systems.
