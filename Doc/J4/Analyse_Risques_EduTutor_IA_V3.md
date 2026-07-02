# Analyse des risques
## Projet : EduTutor IA

**Version :** J4 – Analyse des risques  
**Contexte :** Suite aux perturbations J3 (Prompt Injection) et J4 (montée en charge, RGAA, internationalisation).

---

# Objectif

Identifier les principaux risques pouvant impacter la plateforme EduTutor IA et proposer des mesures de réduction afin d'assurer la sécurité, la conformité et la disponibilité du service.

---

# Méthodologie

Chaque risque est évalué selon deux critères :

- **Probabilité** : Faible / Moyenne / Élevée
- **Impact** : Faible / Moyen / Élevé

La criticité est déterminée à partir de ces deux indicateurs.

| Couleur | Niveau |
|---------|--------|
| 🟢 | Faible |
| 🟡 | Modéré |
| 🟠 | Important |
| 🔴 | Critique |

---

# Synthèse des risques

| ID | Risque | Probabilité | Impact | Criticité | Mesures proposées |
|----|---------|-------------|--------|-----------|-------------------|
| R1 | Prompt Injection lors de l'import d'un document | Élevée | Élevé | 🟢 Critique | Prompt système défensif, filtrage des documents, validation des sorties |
| R2 | Non-conformité au RGAA | Moyenne | Élevé | 🔴 Critique | Audit RGAA, navigation clavier, contraste, textes alternatifs, tests lecteurs d'écran |
| R3 | Saturation des serveurs lors d'un pic de connexions | Élevée | Très élevé | 🔴 Critique | Architecture scalable, load balancer, mise en cache, autoscaling |
| R4 | Réponses IA incorrectes lors de l'internationalisation | Moyenne | Moyen | 🟠 Important | Détection de langue, prompts adaptés, validation des traductions |
| R5 | Fuite ou compromission des données personnelles | Faible | Très élevé | 🔴 Critique | Chiffrement, contrôle des accès, journalisation, conformité RGPD |

---

# Analyse détaillée

## R1 – Prompt Injection

### Description
Un utilisateur malveillant peut intégrer des instructions cachées dans un document afin de modifier le comportement du modèle de langage.

### Conséquences
- Quiz erronés
- Perte de confiance
- Contournement des règles métier

### Mesures
- Prompt système défensif
- Filtrage des documents
- Validation des réponses générées
- Tests OWASP LLM Top 10

---

## R2 – Non-conformité RGAA

### Description
La plateforme pourrait ne pas être utilisable par les personnes en situation de handicap.

### Conséquences
- Non-respect des exigences du sponsor
- Exclusion de certains utilisateurs
- Risque juridique

### Mesures
- Audit RGAA
- Navigation au clavier
- Contraste suffisant
- Compatibilité avec les lecteurs d'écran

---

## R3 – Montée en charge

### Description
Une forte augmentation du nombre d'utilisateurs peut provoquer une saturation des ressources.

### Conséquences
- Temps de réponse élevés
- Indisponibilité du service
- Dégradation de l'expérience utilisateur

### Mesures
- Architecture scalable
- Load Balancer
- Cache
- Autoscaling
- Supervision des performances

---

## R4 – Internationalisation

### Description
Les réponses du LLM peuvent être inadaptées ou incorrectes dans certaines langues.

### Conséquences
- Mauvaise compréhension
- Dégradation de la qualité pédagogique

### Mesures
- Détection automatique de la langue
- Prompts adaptés par langue
- Validation des contenus générés

---

## R5 – Données personnelles

### Description
Les comptes utilisateurs et documents importés contiennent des données sensibles.

### Conséquences
- Violation du RGPD
- Perte de confiance
- Sanctions réglementaires

### Mesures
- Chiffrement des données
- Gestion des droits d'accès
- Sauvegardes
- Journalisation des accès

---

# Matrice Probabilité × Impact

| Impact \\ Probabilité | Faible | Moyenne | Élevée |
|------------------------|:------:|:-------:|:------:|
| **Faible** | 🟢 | 🟢 | 🟡 |
| **Moyen** | 🟢 | 🟡 | 🟠 |
| **Élevé** | 🟡 | 🟠 | 🔴 |

Positionnement des risques :

- **R1** → 🔴
- **R2** → 🔴
- **R3** → 🔴
- **R4** → 🟡
- **R5** → 🔴

---

# Conclusion

L'analyse met en évidence que les risques les plus critiques concernent la sécurité du modèle de langage, la montée en charge de la plateforme, l'accessibilité (RGAA) et la protection des données personnelles. Les mesures proposées permettront d'améliorer la résilience, la conformité et la fiabilité d'EduTutor IA face à son évolution vers une plateforme nationale.
