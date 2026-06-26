# Nike Mind — corrected flow after production rollback

- Production theme rollback verified.
- CRO implementation placed on dev theme only.
- No production merge performed.

Preview: https://lksneakers.com.br/collections/nike-mind-001?preview_theme_id=155065450718

{
  "utc": "20260607T131641Z",
  "corrective_action": "Production theme rolled back; implementation moved to dev theme only. No merge to production performed.",
  "prod_theme": 155065417950,
  "dev_theme": 155065450718,
  "prod_checks_after_rollback": {
    "snippets/lk-goc-collection.liquid": {
      "sha": "26413865cafbb2d7e2e09c8c2ca8747810b43a91910f76a6c5bab15f15c4a8c9",
      "has_cta": false,
      "has_fallback_marker": false,
      "has_nike_branch": false
    },
    "sections/lk-collection.liquid": {
      "sha": "d0162a8482fab762b3aad2e8a73e3e18566ceb555f5ab5b4ab06410f6850f80a",
      "has_cta": false,
      "has_fallback_marker": false,
      "has_nike_branch": true
    }
  },
  "dev_results": [
    {
      "key": "snippets/lk-goc-collection.liquid",
      "source_candidate": "/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-production/nike-mind-approved-3-20260607T123858Z/after__snippets__lk-goc-collection.liquid",
      "before_sha": "f121ba0dafffef8e7bba2bb3ddda84f1a35f80093461e6ffdb23c9effa3854c0",
      "candidate_sha": "0b0857c4b88480b862f867241f6b0ff8e15f0a0a57d35cd791120b1261a115f2",
      "readback_sha": "0b0857c4b88480b862f867241f6b0ff8e15f0a0a57d35cd791120b1261a115f2",
      "restored_to_dev_ok": true,
      "has_cta": true,
      "has_selection": true,
      "has_human": true,
      "has_fallback_marker": false
    },
    {
      "key": "sections/lk-collection.liquid",
      "source_candidate": "/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-production/nike-mind-approved-3-20260607T123858Z/after3__sections__lk-collection.liquid",
      "before_sha": "f8101e2e1ab4b37e0b334b01636fd53358a32393e6bc97074ca466a159359f2c",
      "candidate_sha": "73f335fa1c7db2f0f081f7420005ec161cc12092a64a36e48681b471f5eb1c01",
      "readback_sha": "73f335fa1c7db2f0f081f7420005ec161cc12092a64a36e48681b471f5eb1c01",
      "restored_to_dev_ok": true,
      "has_cta": true,
      "has_selection": true,
      "has_human": true,
      "has_fallback_marker": true
    }
  ],
  "preview_url": "https://lksneakers.com.br/collections/nike-mind-001?preview_theme_id=155065450718"
}