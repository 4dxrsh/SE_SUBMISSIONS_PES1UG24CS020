# SE_LAB1_PES1UG24CS020
# Hospital Bed & ICU Allocation Dashboard
**Lab 1 — Requirements Engineering & UML Use-Case Modelling | Problem Statement #20**

An ER bed management dashboard displaying real-time ward occupancy, prioritizing ICU transfers based on triage score, and orchestrating inter-facility ambulance transfer workflows.

**Stakeholders / Actors:** Triage Nurse, Hospital Administrator, Ambulance Dispatch System (external)

## Repository Structure
```
hospital-bed-icu-dashboard/
├── README.md
├── requirements.docx                      # 5 FRs + 2 NFRs
├── diagrams/
│   ├── use-case-diagram.pdf               # Final UML use-case diagram (submit this)
│   ├── use-case-diagram.svg               # Same diagram, source image
│   └── use-case-diagram.puml              # Editable PlantUML source (optional)
└── docs/
    └── use-case-flow-icu-transfer.docx    # 1-page flow spec for "Initiate ICU Transfer Request"
```

## Deliverables Checklist
- [x] Requirements table — Exactly FR-001 to FR-005, plus NFR-001 & NFR-002, each with ID, Type, Description, Priority, Acceptance Criteria, Rationale → [`requirements.docx`](./requirements.docx)
- [x] UML Use-Case Diagram — all actors, primary use cases, at least one `«include»` and one `«extend»` → [`diagrams/use-case-diagram.pdf`](./diagrams/use-case-diagram.pdf)
- [x] Use-Case Flow Specification (1 page) — Preconditions, Postconditions, Main Success Scenario, one Alternate Flow → [`docs/use-case-flow-icu-transfer.docx`](./docs/use-case-flow-icu-transfer.docx)

## Diagram Summary
- **`«include»`**: *Log Patient Intake & Vitals* includes *Compute Triage Severity Score* — the score is always computed as part of logging intake, so it's mandatory, not optional.
- **`«extend»`**: *Request Inter-Facility Ambulance Transfer* extends *Initiate ICU Transfer Request* at the extension point **"No Local ICU Bed Available"** — it only runs conditionally, when no local ICU bed exists.