# Mise à jour des Personas – Perturbations APOCAL'IPSSI

## Objectif

Au fil des perturbations du projet, les besoins des utilisateurs ont évolué. Les personas ont donc été mis à jour afin de refléter les nouvelles contraintes fonctionnelles et non fonctionnelles introduites durant le développement.

---

# Persona 1 – Stephanie Martin
### Étudiante en Licence

## Nouveaux besoins identifiés

### Perturbation J2 – Performance
- Génération rapide des quiz.
- Temps d'attente réduit afin d'éviter l'abandon de l'application.

**Impact**
> Stephanie souhaite obtenir ses quiz en quelques secondes afin de conserver une expérience fluide.

### Perturbation J3 – Sécurité IA
- Les réponses générées ne doivent pas pouvoir être manipulées par des attaques de Prompt Injection.
- Les quiz doivent rester fiables même si le document contient du contenu malveillant.

**Impact**
> Stephanie doit pouvoir faire confiance aux questions générées automatiquement.

### Perturbation J3-bis – RGPD
- Pouvoir demander la suppression ou l'export de ses données personnelles.
- Garantir la confidentialité de ses documents.

**Impact**
> Stephanie souhaite conserver le contrôle de ses données personnelles.

### Perturbation J4 – Scalabilité, Accessibilité et Internationalisation
- Interface disponible dans plusieurs langues (i18n).
- Application compatible avec les standards d'accessibilité (RGAA).
- Temps de réponse conservé même avec un grand nombre d'utilisateurs.

**Impact**
> Stephanie peut utiliser la plateforme quelle que soit sa langue ou ses besoins d'accessibilité.

---

# Persona 2 – Sophie Lefèvre
### Enseignante

## Nouveaux besoins identifiés

### Perturbation J2
- Génération rapide des quiz pour préparer ses cours.
- Réduction des temps d'attente.

### Perturbation J3
- Les contenus générés doivent rester fiables.
- Les étudiants ne doivent pas pouvoir influencer les réponses du LLM via des documents malveillants.

### Perturbation J3-bis
- Garantir la conformité RGPD des documents déposés.
- Possibilité d'exporter ou supprimer les données associées à un étudiant.

### Perturbation J4
- Pouvoir partager les quiz avec des étudiants internationaux.
- Interface accessible à tous les profils d'étudiants.
- Disponibilité de la plateforme même lors de fortes périodes d'utilisation.

---

# Persona 3 – Jean Moreau
### Administrateur système

## Nouveaux besoins identifiés

### Perturbation J2
- Surveiller les performances du système.
- Optimiser le choix du modèle LLM.
- Réduire les coûts d'exécution.

### Perturbation J3
- Mettre en place des protections contre les Prompt Injections.
- Ajouter des validations des réponses générées.
- Journaliser les incidents de sécurité.

### Perturbation J3-bis
- Respect des exigences RGPD.
- Gestion des demandes d'export et de suppression des données.
- Traçabilité des traitements.

### Perturbation J4
- Préparer la plateforme à une montée en charge nationale.
- Garantir la haute disponibilité.
- Déployer une architecture scalable.
- Assurer la conformité RGAA.
- Prévoir le support multilingue (i18n).

---

# Synthèse des évolutions

| Perturbation | Impact sur les personas |
|--------------|-------------------------|
| J2 | Performance et réduction du temps de génération des quiz. |
| J3 | Sécurisation des modèles LLM contre les Prompt Injections et amélioration de la fiabilité des réponses. |
| J3-bis | Conformité RGPD, gestion des données personnelles et traçabilité. |
| J4 | Scalabilité, accessibilité (RGAA), internationalisation (i18n) et disponibilité du service. |

---

# Conclusion

Les personas ont évolué afin de prendre en compte les nouvelles exigences rencontrées pendant le projet.

Ces mises à jour permettent de conserver des profils utilisateurs cohérents avec les décisions prises lors des différentes perturbations et justifient les choix techniques réalisés au cours du développement.
