# ERP

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 11.2.3

## Permissions
####  Permission system
the permissions structure: `Role` => `Permissions` => `{ PermissionType, PermissionGroup}`

##### Configured PermissionGroups
| GroupeID      | Name          |
| ------------- |:-------------:|
|1| Client|
|2| Bailleur de Fonds|
|3| Partenaire|
|4| Opportunite|
|5| Personnes De Contact|
|6| Influenceur|
|7| Consultant|
|8| Sous-traitant|
|9| Document de Référence|
|10| Domaine|
|11| CV|
|12| Reference|
|13| Manifestation|
|14| Utilisateurs|
|15| Dashboard|

##### Configured PermissionTypes
| TypeID      | Name          |
| ------------- |:-------------:|
|1| Afficher le tableau de bord|
|2| Ajouter|
|3| Modifier|
|4| Supprimer|
|5| Imprimer Liste|
|6| Imprimer|
|7| Exporter BD|
|8| Revue|
|9| Analyse|
|10| Approbation|
|11| Préparation du dossier|
|12| Affecter Responsable|
|13| Verification|

####  `[hasPermission]` directive :

  Input: `string` or `string[]`

  Exemple Role: `['1_5']`

  Usage: `<div *hasPermission="['1_5']"> ... </div>`

  If the user has that particulier permission/ permissions the Element will be rendered

## Company 

DNDSERV (Digital and Design)

## Developers 
Bedoui Oussama ( Fullstack Web Angular Node.je Developer ) 
    Email: oussama.bedoui@gmail.com
    LinkedIn: https://www.linkedin.com/in/oussama-bedoui-26167212b/

Bedoui Jesser ( Fullstack Web Angular Node.je Developer )
    Email: bedouijesser@gmail.com
    LinkedIn: https://www.linkedin.com/in/jesser-bedoui-659805172/

Yosra Bouajeja ( Fullstack Web Angular Node.je Developer )
    Email: N/A
    LinkedIn: N/A
    
