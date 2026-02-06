from sample_data import load_sample_manuals
from impact_engine import ImpactAssessmentEngine
from compliance import ComplianceManager


def submit_design_change():
    print("\n--- Submit Design Change ---")
    change_id = input("Enter Change ID (SB/MOD ref): ")
    ata = input("Enter Affected ATA Chapter: ")
    config = input("Enter Aircraft Configuration: ")

    return {
        "id": change_id,
        "ata": ata,
        "configuration": config
    }


def main():
    print("=== Aircraft Technical Documentation Impact Manager ===")

    manuals = load_sample_manuals()
    engine = ImpactAssessmentEngine()
    compliance = ComplianceManager()

    print("\nLoaded Manuals:")
    for m in manuals:
        print(m)

    change = submit_design_change()

    impacted = engine.assess_impact(change, manuals)

    if not impacted:
        print("\nNo manuals impacted.")
        return

    print("\n--- Impact Assessment Results ---")
    for manual in impacted:
        print(f"\nImpacted: {manual}")
        actions = engine.determine_actions()
        for action in actions:
            print(f"- {action}")

        config_status = compliance.verify_configuration(manual, change)
        print(f"- {config_status}")

        manual.update_revision(change["id"])

    print("\n--- Updated Manuals ---")
    for m in manuals:
        print(m)


if __name__ == "__main__":
    main()
