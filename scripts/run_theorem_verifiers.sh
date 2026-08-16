#!/bin/sh
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)

python3 "$SCRIPT_DIR/verify_public_hash_entropy.py"
python3 "$SCRIPT_DIR/verify_fixed_slot_integer_code.py"
python3 "$SCRIPT_DIR/verify_poisson_phase_analytic.py"
python3 "$SCRIPT_DIR/verify_poisson_root_certificate.py"
python3 "$SCRIPT_DIR/verify_poisson_phase_transition.py"
python3 "$SCRIPT_DIR/verify_cross_block_mod6_construction.py"
python3 "$SCRIPT_DIR/verify_two_subblock_modulus_sharp_converse.py"
python3 "$SCRIPT_DIR/verify_operational_support_completion_small.py"
python3 "$SCRIPT_DIR/verify_joint_replacement_rank_volume_small.py"
