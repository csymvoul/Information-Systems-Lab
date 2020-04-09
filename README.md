# Εργαστήριο Πληροφοριακών Συστημάτων

Το συγκεκριμένο project αφορά το εργαστήριο του μαθήματος __«(ΨΣ-152) Πληροφοριακά Συστήματα»__ του τμήματος __Ψηφιακών Συστημάτων__ του __Πανεπιστημίου Πειραιώς__. 

Μπορείτε να βρείτε το κώδικα από τις διαφάνειες του μαθήματος χωρισμένο σε διαφορετικούς φακέλους. 

## Δομή του εργαστηρίου
1. [Εργαστήριο 1 - Εισαγωγή Εισαγωγή στην Υπηρεσιοστρεφή Αρχιτεκτονική και τη Python](https://github.com/csymvoul/Information-Systems-Lab/tree/master/lab1)
   * Εισαγωγή με την Υπηρεσιοστρεφή Αρχιτεκτονική (SOA) και τα Web Services
      * SOA
      * REST & Restful APIs
   * Γνωριμία με τη Python 3
      * Γενικές έννοιες
      * Anaconda distribution
   * Git
      * GitΗub account
      * Δημιουργία νέου repository
      * Βασικές εντολές
2. [Εργαστήριο 2 - Εισαγωγή στο Docker](https://github.com/csymvoul/Information-Systems-Lab/tree/master/lab2)
   * Docker - Βασικές έννοιες 
   * Πλεονεκτήματα και Μειονεκτήματα
   * Εγκατάσταση Docker
   * Εκτέλεση εφαρμογών 
   * Docker containers networking
   * Docker Hub 
3. [Εργαστήριο 3 - MongoDB και Flask 1/2](https://github.com/csymvoul/Information-Systems-Lab/tree/master/lab3)
4. Εργαστήριο 4 - MongoDB και Flask 2/2
5. Εργαστήριο 5 - Containerization

### Εγκατάσταση Python 3
Προτείνεται η χρήση της διανομής Anaconda. Παρακάτω μπορείτε να βρείτε και τα link για να κατεβάσετε τη Python: 
* Python 3: https://www.python.org/downloads/
* Anaconda: https://www.anaconda.com/distribution/

#### Εγκατάσταση Anaconda: 
Για χρήστες Windows: Κατά την εγκατάσταση προτείνεται η επιλογή της εισαγωγής της Anaconda στο system PATH. Εναλλακτικά θα πρέπει να την εισάγεται χειροκίνητα όπως παρακάτω:

1. Ανοίγουμε το CMD με δικαιώματα Διαχειριστή 
2. Βρίσκουμε που έχει εγκατασταθεί η Python με την εντολή: ```where python```
3. Κάνουμε copy το path και εκτελούμε την εντολή: ```set PATH=python_path;%PATH%```
    * Όπου ```python_path``` είναι το path της εγκατάστασης της Python που βρήκαμε στο βήμα 2

#### Γενικές έννοιες: 
* Τα αρχεία Python πρέπει να έχουν πάντα τη κατάληξη .py: `file_name.py`

##### Python Virtual Environments 
Ένα Python Virtual Environment είναι εργαλείο που βοηθάει στη διατήρηση των dependencies που 
απαιτούνται από διαφορετικές εφαρμογές. 

__virtualenv__
  * Πρέπει πρώτα να γίνει εγκατάσταση του virtualenv:	``pip install virtualenv``
  * Δημιουργία Virtual Environment: `virtualenv venv_name`
  * Ενεργοποίηση περιβάλλοντος:	`source path/to/venv_name activate`
  * Απενεργοποίηση περιβάλλοντος:	`deactivate` 

__conda environment__
  * Δημιουργία Conda περιβάλλοντος: `conda create --name infosys`
  * Ενεργοποίηση περιβάλλοντος: `conda activate infosys`
  * Απενεργοποίηση περιβάλλοντος: `conda deactivate`

##### Εγκατάσταση βιβλιοθηκών και πακέτων
Πρέπει να έχετε εγκαταστήσει το ```pip```. 
* Mπορείτε να εγκαταστήσετε και να χρησιμοποιήσετε βιβλιοθήκες απλά εκτελώντας την εντολή:
  * ```pip install packagename```
  * _Μόνο για χρήστες Anaconda:_ ```conda install packagename```

Όταν τις κάνουμε εγκατάσταση σε κάποιο περιβάλλον, μπορούμε να τις εισάγουμε σε κάποιο πρόγραμμά μας έτσι: 
```import package_name```

_Αν θέλουμε να κάνουμε εγκατάσταση ένα package σε ένα virtual environment __πρέπει πρώτα να το ενεργοποιήσουμε__!_

##### Εγκατάσταση και Export requirement
* Τα requirement είναι οι βιβλιοθήκες που είναι αναγκαίες για να λειτουργήσει το python project μας.
* Για να τα κάνουμε export σε ένα αρχείο χρησιμοποιούμε την εντολή: 
  * `pip freeze > requirements.txt` 
  * _Μόνο για χρήστες Anaconda_: `conda list --export > requirements.txt`
* Για νά κάνουμε εγκατάσταση τα requirement από ένα αρχείο χρησιμοποιούμε την εντολή: 
  * `pip install -r  > requirements.txt` 
  * _Μόνο για χρήστες Anaconda_: `conda install --file requirements.txt`

## Στοιχεία επικοινωνίας
* Χρυσόστομος Συμβουλίδης, simvoul@unipi.gr
* Jean-Didier Totow, totow@unipi.gr 
