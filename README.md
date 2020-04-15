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

## Python 3
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
  * Δημιουργία Conda περιβάλλοντος: `conda create --name conda_env`
  * Ενεργοποίηση περιβάλλοντος: `conda activate conda_env`
  * Απενεργοποίηση περιβάλλοντος: `conda deactivate`

##### Εγκατάσταση βιβλιοθηκών και πακέτων
Πρέπει να έχετε εγκαταστήσει το ```pip```. 
* Mπορείτε να εγκαταστήσετε και να χρησιμοποιήσετε βιβλιοθήκες απλά εκτελώντας την εντολή:
  * ```pip install packagename```
  * _Μόνο για χρήστες Anaconda_: 
    * ```conda install packagename```
    * __Σημείωση: Δεν είναι όλα τα packages διαθέσιμα στο conda!__
    * Αν θέλουμε να κάνουμε εγκατάσταση κάτι μέσω `pip` Anacona Virtual Environment μας __πρώτα κάνουμε εγκατάσταση το pip__ στο environment και μετά κατεβάζουμε τα packages που θέλουμε: 
      1. ```conda install pip```
      2. ```pip install packagename```

Όταν τις κάνουμε εγκατάσταση σε κάποιο περιβάλλον, μπορούμε να τις εισάγουμε σε κάποιο πρόγραμμά μας έτσι: 
```import package_name```

_Αν θέλουμε να κάνουμε εγκατάσταση ένα package σε ένα virtual environment __πρέπει πρώτα να το ενεργοποιήσουμε__!_

##### Εγκατάσταση και Export requirement
* Τα requirement είναι οι βιβλιοθήκες που είναι αναγκαίες για να λειτουργήσει το python project μας.
* Για να τα κάνουμε export σε ένα αρχείο χρησιμοποιούμε την εντολή: 
  * `pip freeze > requirements.txt` 
  * _Μόνο για χρήστες Anaconda_: `conda list --export > requirements.txt`
* Για νά κάνουμε εγκατάσταση τα requirement από ένα αρχείο χρησιμοποιούμε την εντολή: 
  * `pip install -r requirements.txt` 
  * _Μόνο για χρήστες Anaconda_: `conda install --file requirements.txt`

## Docker 

#### Εγκατάσταση Docker 
##### Απαιτήσεις συστήματος: 
__Hardware__:
* 64-bit processor με Second Level Address Translation (SLAT)
* 4GB system RAM
* BIOS-level hardware virtualization support πρέπει να είναι ενεργοποιημένο στις ρυθμίσεις του BIOS (συνήθως είναι ήδη activated)

__Εγκατάσταση στα Windows__: 
* Πρέπει να έχετε Windows 10 Pro, Windows 10 Student edition - Σε Windows Home δεν θα μπορέσει να γίνει εγκατάσταση σωστά
* Πρέπει επίσης να είναι ενεργοποιημένα τα: 
  * Hyper-V 
  * Containers Windows Features
* Κατεβάζετε το εκτελέσιμο αρχείο από εδώ: https://hub.docker.com/editions/community/docker-ce-desktop-wind
ows

__Εγκατάσταση στα Linux (Ubuntu)__:
* Αρκεί να εκτελέσετε τις παρακάτω εντολές στο terminal: 
  * `sudo apt-get update`
  * `sudo apt install -y apt-transport-https ca-certificates curl software-properties-common`
  * `curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`
  * `sudo add-apt-repository -y "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"`
  * `sudo apt-get update`
  * `sudo apt install docker-ce`

#### Βασικές εντολές Docker

* Προβολή λίστας με όλα τα images που έχουμε τοπικά στον υπολογιστή μας: `docker images`
* Εμφάνιση λίστας με όλα τα container που έχουμε στον υπολογιστή μας: `docker ps -a`
* Δημιουργία και εκτέλεση container (Αν δεν υπάρχει ήδη τοπικά στον υπολογιστή, θα γίνει και κατέβασμα): `docker run image_name --name friendly_name -p HOST_PORT:DOCKER_PORT`
* Εκτέλεση εντολών μέσα σε ένα container: `docker exec friendly_name`
* Παύση ενός container: `docker stop friendly_name`
* Αφαίρεση ενός σταματημένου container: `docker rm friendly_name` 
* Διαγραφή ενός image από τον υπολογιστή (αφού πρώτα έχει διαγραφεί το container που το χρησιμοποιεί): `docker rmi image_name`
* Εμφάνιση low-level πληροφοριών για ένα container: `docker inspect friendly_name`
* Εμφάνιση log για ένα container: `docker log friendly_name`
* Build από Dockerfile: `docker build -t image_name .`
  * `.` στο τέλος βάζουμε αν το Dockerfile είναι στο ίδιο μέρος με το path που έχουμε στο terminal. 
  * Ενναλακτικά, αντικαθιστούμε το `.` με το path για το Dockerfile

#### Δημιουργία Dockerfile
_Προσοχή: Το Dockerfile δεν έχει κάποιο extension!_

__Linux__: 
* Για να το δημιουργήσουμε πρέπει να εκτελέσουμε τη παρακάτω εντολή στο terminal: `touch Dockerfile`

__Windows__:
* Δημιουργούμε ένα κενό txt αρχείο (πχ στο Notepad) και το αποθηκεύουμε χωρίς extension: 
    * File / Save as / File name: Dockerfile 
    * Και επιλέγουμε Save as type: All Files (\*.\*)

__Βασικές εντολές που θα χρησιμοποιήσουμε σε ένα Dockerfile__:
* Ποια είναι η base image που χρησιμοποιείται (πρέπει __πάντα να υπάρχει σε ένα Dockerfile__ και το βάζουμε στη __πρώτη γραμμή__): `FROM ubuntu:16.04` 
* Όνομα και email του maintainer του image: `MAINTAINER name <email@address.domain>`
* Αντιγραφή αρχείων από τον host στο container: `COPY filename /dir/to/docker/container`
* Προεπιλογές για την εκτέλεση ενός container: `CMD command`
* Εκτέλεση εντολών μέσα στο container: `RUN command`
* Ποιες port κάνει expose το container: `EXPOSE 80/tcp`
* Κάνουμε set τον χρήστη: `USER username`
* Τρέχει όταν ξεκινήσει το container: `ENTRYPOINT [“executable”,”param1”,”param2”]` 

## Στοιχεία επικοινωνίας
* Χρυσόστομος Συμβουλίδης, simvoul@unipi.gr
* Jean-Didier Totow, totow@unipi.gr 
