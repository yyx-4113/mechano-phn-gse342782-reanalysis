# C2 — Domain review (mechanotransduction / PHN neuroscience)

**Reviewer:** C2 (independent domain expert; first-exposure review of v1.1.8)

## Scope of this review

I reviewed the manuscript as a new submission, with no knowledge of prior rounds. My brief: is the science coherent, are the claims calibrated to the evidence, and is anything in the domain handling wrong or overstated?

## What the paper shows (as I read it)

In a frozen-panel reanalysis of GSE342782, the pre-specified primary endpoint (ECM-integrin-Hippo module M3 under acute-HZ serum exosomes) is a bounded null (MDE 0.18 log2CPM). The positive signal is a gene-level, family-corrected suppression of the electrochemical nociceptor module E1 led by TRPV1, with no M1 (mechanogated) gene reaching significance; a route-by-program difference-in-differences (−0.193; exact permutation P = 0.0011) supports route dependence. Every module-level selectivity claim is explicitly downgraded to nominal/gene-level status because the E1≫M1 interaction does not survive restriction to detected genes.

## Findings

**1. Internal calibration of claims is unusually disciplined — no domain objection.** The places where this paper could most easily over-claim (module-level E1 selectivity; "VZV effects"; PIEZO2 as the allodynia-relevant mechanogate; ESWT as mechanistic support) are each explicitly fenced:
- The E1 selectivity is stated as gene-level/nominal three separate times (§3.3, §3.4, §4.2) and never as a confirmed dissociation. Consistent.
- The M1 null is explicitly *not* read as evidence against a mechanical axis, with the post-translational-regulation argument spelled out (§4.1) — exactly the right move given the Piezo2 voltage-block literature. The escape hatch is earned, not asserted: the same decoupling logic that licenses the E1-direction reconciliation is applied to M1.
- ESWT is quarantined as contextual background, with the explicit statement that no cited work tested a YAP/TAZ or neuronal-channel mechanism in PHN (§4.3) and that the largest RCT showed no significant time-by-group interaction (§1, §4.3). Correct and appropriately conservative.
- The PHN-exosome contrast is reported as non-specific and donor-confounded and is excluded from all confirmatory use (§3.5, §5).

**2. Domain accuracy of the specific claims I checked — all pass.** Piezo2 as the major transducer of touch and its gain-of-function sensitization of nociceptors (^18-21^); human PIEZO2 loss-of-function as "selective loss of discriminative touch and proprioception" (^23^) — the Chesler 2016 claim is stated accurately, not as "loss of all touch"; SCN9A loss-of-function congenital insensitivity to pain (^24^); the Sánchez-Carranza voltage-block mechanism (^21^) is the correct citation for post-translational Piezo2 regulation. The rESWT citation is used for a compartmental argument (non-neuronal ATP/P2X7R/p38MAPK EV release in a rat bone-callus model), which is what that dataset supports.

**3. The §4.1 directionality reconciliation is biologically sound.** All three offered reconciliations (mRNA–function decoupling; exosome as host-signal readout; embryonic-clone model limitation) are live hypotheses in the field, and the paper explicitly declines to choose among them. The added balance — that genuinely counter-regulatory/homeostatic down-regulation remains open — is the honest framing.

**4. One domain-level flag (non-blocking, for the record): §3.3's section title.** "HZ-serum exosomes suppress electrochemical nociceptor channels" states the module-level suppression as fact, while the section body itself repeatedly qualifies it as a module-level signal whose selectivity is nominal/gene-level once detection-floor asymmetry and neutral controls are considered. The abstract, §3.4 and §4.2 all carry the qualifiers. I do not require a title change (JPR section titles are routinely declarative, and the body immediately qualifies), but a future revision could read "…suppress the electrochemical nociceptor module at the module level; gene-level selectivity remains nominal". Recording as an observation, not a revision demand.

**5. Limitations inventory is complete for this design.** The sixteen numbered constraints cover model (i–ii), composition/post-translational blindness (iii), donor confounding (iv), detection-floor scope limits (v), borderline direct-infection effect (vi), hypothesis-generating status (vii), exosome-identity caveat (viii), cross-experiment baseline drift (ix), non-reproduction of the source study's substance-P finding (x), neutral-control non-separability (xi), substrate stiffness (xii), missing compartments and dose (xiii), scoring-function conditionality (xiv), transcript-only readout (xv), and replicate independence (xvi). I would have expected (xi) and (xii); all sixteen are correctly placed.

## Verdict

No domain objections to acceptance. One required fix exists elsewhere in this round (C1's comma, §3.1); one non-blocking title observation is logged above for the author's discretion at proof stage.
