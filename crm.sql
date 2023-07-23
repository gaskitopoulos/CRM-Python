-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Εξυπηρετητής: 127.0.0.1
-- Χρόνος δημιουργίας: 27 Φεβ 2023 στις 20:36:44
-- Έκδοση διακομιστή: 10.4.24-MariaDB
-- Έκδοση PHP: 7.4.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Βάση δεδομένων: `crm`
--

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `αιτήσεις`
--

CREATE TABLE `αιτήσεις` (
  `Κωδικός_Αίτησης` int(11) NOT NULL,
  `Διεύθυνση_Αλλ` varchar(40) DEFAULT NULL,
  `Διεύθυνση_Παροχής` varchar(40) DEFAULT NULL,
  `Κωδικός_Επαφής` int(11) DEFAULT NULL,
  `Ρεύμα_Αέριο` varchar(10) DEFAULT NULL,
  `Κατηγορία_Τιμολόγησης` varchar(5) DEFAULT NULL,
  `Εγγύηση` int(11) DEFAULT NULL,
  `Πρόγραμμα` varchar(25) DEFAULT NULL,
  `Τύπος_Ενεργοποίησης` varchar(25) NOT NULL,
  `ΤΚ_Αλλ` varchar(5) NOT NULL,
  `Πόλη_Αλλ` varchar(25) NOT NULL,
  `ΤΚ_Παροχής` varchar(5) NOT NULL,
  `Πόλη_Παροχής` varchar(25) NOT NULL,
  `ebill` varchar(5) NOT NULL,
  `Ημερομηνία` date NOT NULL DEFAULT current_timestamp(),
  `Κωδικός_Πωλητή` varchar(3) NOT NULL,
  `Λίστα` varchar(5) NOT NULL,
  `Πάγια_Εντολή` varchar(5) NOT NULL,
  `Κατηγορία_Πελάτη` varchar(25) NOT NULL,
  `Σχόλια_Ραντεβού` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Άδειασμα δεδομένων του πίνακα `αιτήσεις`
--

INSERT INTO `αιτήσεις` (`Κωδικός_Αίτησης`, `Διεύθυνση_Αλλ`, `Διεύθυνση_Παροχής`, `Κωδικός_Επαφής`, `Ρεύμα_Αέριο`, `Κατηγορία_Τιμολόγησης`, `Εγγύηση`, `Πρόγραμμα`, `Τύπος_Ενεργοποίησης`, `ΤΚ_Αλλ`, `Πόλη_Αλλ`, `ΤΚ_Παροχής`, `Πόλη_Παροχής`, `ebill`, `Ημερομηνία`, `Κωδικός_Πωλητή`, `Λίστα`, `Πάγια_Εντολή`, `Κατηγορία_Πελάτη`, `Σχόλια_Ραντεβού`) VALUES
(6, 'Βενιζέλου 1', 'Ποτίδαια', 36, 'ΡΕΥΜΑ', 'Γ1', 50, 'POWER HOME BASIC', 'Αλλαγή Παρόχου', '54629', 'Θεσσαλονίκη', '63200', 'Ποτίδαια', 'Ναι', '2023-01-28', '006', 'HSH', 'Ναι', '', ''),
(13, 'ΠΑΠΑΓΟΥ 32', 'ΠΑΠΑΓΟΥ 32', 43, 'ΡΕΥΜΑ', 'Γ1Ν', 50, 'POWER HOME BASIC', 'Αλλαγή Παρόχου', '13452', 'ΑΙΓΑΛΕΩ', '13452', 'ΑΙΓΑΛΕΩ', 'Όχι', '2023-01-31', '008', 'HSH', 'Ναι', '', ''),
(21, 'Βέροιας 1', 'Βέροιας 1', 36, 'ΡΕΥΜΑ', 'Γ1Ν', 50, 'POWER HOME BASIC', 'Αλλαγή Παρόχου', '59100', 'Βέροια', '59100', 'Βέροια', 'Ναι', '2023-02-07', '008', 'HSH', 'Ναι', '', ''),
(31, 'ΠΑΠΑΓΟΥ 2', 'ΠΑΠΑΓΟΥ 80', 51, 'ΡΕΥΜΑ', 'Γ1Ν', 50, 'POWER HOME BASIC', 'ΑΛ. ΠΑΡΟΧΟΥ', '55535', 'ΠΥΛΑΙΑ', '55535', 'ΠΥΛΑΙΑ', 'Ναι', '2023-02-08', '008', 'HSH', 'Ναι', 'ΙΔΙΩΤΗΣ', 'ΡΑΝΤΕΒΟΥ'),
(33, 'ΣΒΩΛΟΥ 6', 'ΞΥΛΟΚΑΣΤΡΟ', 54, 'ΡΕΥΜΑ', 'Γ1Ν', 50, 'POWER HOME BASIC', 'ΕΠΑΝΑΣΥΝΔΕΣΗ', '54623', 'ΘΕΣΣΑΛΟΝΙΚΗ', '20400', 'ΞΥΛΟΚΑΣΤΡΟ', 'Ναι', '2023-02-08', '018', 'CC', 'Ναι', 'ΙΔΙΩΤΗΣ', '9/2/2023 10-13\nΔΙΝΕΙ ΛΟΓΑΡΙΑΣΜΟ ΚΑΙ ΕΝΔΕΙΞΗ'),
(68, 'ΒΕΝΙΖΕΛΟΥ 1', 'ΠΑΠΑΝΔΡΕΟΥ 2', 36, 'ΑΕΡΙΟ', 'T2', 100, 'GAS HOME EASY', 'Αλλαγή Παρόχου', '56221', 'ΘΕΣΣΑΛΟΝΙΚΗ', '56227', 'ΕΥΟΣΜΟΥ', 'Όχι', '2023-02-12', '016', 'HSH', 'Ναι', '', ''),
(69, 'ΒΕΝΙΖΕΛΟΥ 2', 'ΠΑΠΑΝΔΡΕΟΥ 9', 36, 'ΑΕΡΙΟ', 'T2', 100, 'GAS HOME EASY', 'Αλλαγή Παρόχου', '54894', 'ΘΕΣΣΑΛΟΝΙΚΗ', '56224', 'ΕΥΟΣΜΟΥ', 'Όχι', '2023-02-12', '006', 'HSH', 'Ναι', '', ''),
(70, 'ΚΑΛΑΠΟΘΑΚΗ 7', 'ΣΒΩΛΟΥ 15', 36, 'ΑΕΡΙΟ', 'T2', 100, 'GAS HOME EASY', 'Επανασύνδεση', '54622', 'ΘΕΣΣΑΛΟΝΙΚΗ', '56224', 'ΕΥΟΣΜΟΥ', 'Όχι', '2023-02-12', '016', 'HSH', 'Όχι', '', ''),
(71, 'ΚΑΛΠΑΚΗ 17', 'ΠΙΝΔΟΥ 80', 36, 'ΑΕΡΙΟ', 'T2', 100, 'GAS HOME EASY', 'Επανασύνδεση', '54352', 'ΘΕΣΣΑΛΟΝΙΚΗ', '56625', 'ΝΕΑΠΟΛΗΣ-ΣΥΚΕΩΝ', 'Όχι', '2023-02-12', '016', 'HSH', 'Όχι', '', ''),
(72, 'ΠΑΠΑΝΔΡΕΟΥ 7', 'ΚΑΛΑΠΟΘΑΚΗ 7', 36, 'ΑΕΡΙΟ', 'T2', 100, 'GAS HOME EASY', 'Επανασύνδεση', '56634', 'ΚΟΡΔΕΛΙΟ', '56423', 'ΘΕΣΣΑΛΟΝΙΚΗΣ', 'Όχι', '2023-02-12', '008', 'HSH', 'Όχι', '', ''),
(88, '', '', 10019, 'ΑΕΡΙΟ', '---', 0, '---', '---', '', '', '', '', '---', '2023-02-12', '---', '---', '---', '', ''),
(89, 'ΑΛΕΞΙΟΥ 15', 'ΑΝΑΣΤΑΣΙΟΥ 5', 10019, 'ΑΕΡΙΟ', 'T2', 100, 'GAS HOME EASY', 'Επανασύνδεση', '56625', 'ΣΥΚΙΕΣ', '56728', 'ΝΕΑΠΟΛΗΣ ΣΥΚΕΩΝ', 'Ναι', '2023-02-12', '008', 'HSH', 'Όχι', '', ''),
(90, 'ΑΛΕΞΙΟΥ 15', 'ΠΑΠΑΝΑΣΤΑΣΙΟΥ 8', 10019, 'ΑΕΡΙΟ', 'T2', 100, 'GAS HOME EASY', 'ΠΡΩΤΗ ΕΓΚΑΤΑΣΤΑΣΗ', '56625', 'ΣΥΚΙΕΣ', '11534', 'ΑΘΗΝΩΝ', 'Ναι', '2023-02-12', '016', 'HSH', 'Ναι', '', ''),
(96, 'ΝΙΚΟΛΑΟΥ ΠΑΡΑΣΚΕΥΑ 51', 'ΠΟΤΙΔΑΙΑ', 55, 'ΡΕΥΜΑ', 'Γ1', 50, 'POWER HOME BASIC', 'ΑΛ. ΠΑΡΟΧΟΥ', '56625', 'ΣΥΚΙΕΣ', '63200', 'Ν. ΠΟΤΙΔΑΙΑ', 'Ναι', '2023-02-27', '008', 'HSH', 'Όχι', 'ΙΔΙΩΤΗΣ', 'ΘΑ ΠΑΡΑΛΑΒΕΙ Ο ΙΔΙΟΣ\nΔΙΚΑΙΟΛΟΓΗΤΙΚΑ ΣΤΟ VIBER\nΡΑΝΤΕΒΟΥ 28/2/2023 10-12');

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `επαφές`
--

CREATE TABLE `επαφές` (
  `Κωδικός_Επαφής` int(11) NOT NULL,
  `Ονοματεπώνυμο` varchar(50) NOT NULL,
  `Διεύθυνση` varchar(50) NOT NULL,
  `ΑΦΜ` varchar(9) NOT NULL,
  `ΑΔΤ` varchar(10) DEFAULT NULL,
  `Κινητό` varchar(10) NOT NULL,
  `Σταθερό` varchar(10) DEFAULT NULL,
  `Πόλη` varchar(30) NOT NULL,
  `ΤΚ` varchar(5) NOT NULL,
  `email` varchar(50) NOT NULL,
  `ΔΟΥ` varchar(16) NOT NULL,
  `Ιδιότητα_Πελάτη` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Άδειασμα δεδομένων του πίνακα `επαφές`
--

INSERT INTO `επαφές` (`Κωδικός_Επαφής`, `Ονοματεπώνυμο`, `Διεύθυνση`, `ΑΦΜ`, `ΑΔΤ`, `Κινητό`, `Σταθερό`, `Πόλη`, `ΤΚ`, `email`, `ΔΟΥ`, `Ιδιότητα_Πελάτη`) VALUES
(36, 'ΠΑΠΑΔΌΠΟΥΛΟΣ ΓΙΏΡΓΟΣ', 'ΒΕΝΙΖΈΛΟΥ 1', '123456789', 'ΑΑ 123456', '6912345678', '2310123456', 'ΘΕΣΣΑΛΟΝΊΚΗ', '54629', 'gior@mail.com', 'ΘΕΣΣΑΛΟΝΙΚΗΣ', 'ΙΔΙΟΚΤΗΤΗΣ'),
(43, 'ΑΛΕΞΟΠΟΥΛΟΣ ΝΙΚΟΛΑΟΣ', 'ΠΑΠΑΓΟΥ 32', '012345678', 'ΑΚ000000', '6949000000', '2101234567', 'ΑΙΓΑΛΕΩ', '13452', '', 'ΑΙΓΑΛΕΩ', 'ΙΔΙΟΚΤΗΤΗΣ'),
(51, 'ΑΣΚΗΤΗΣ ΝΙΚΟΛΑΟΣ', 'ΠΑΠΑΝΔΡΕΟΥ 2', '129874563', 'ΑΡ 178562', '6931020304', '', 'ΚΑΛΑΜΑΡΙΑ', '55132', '', 'ΚΑΛΑΜΑΡΙΑΣ', 'ΙΔΙΟΚΤΗΤΗΣ'),
(52, 'ΠΑΠΠΑ ΜΑΡΙΑ', 'ΣΚΡΑ 7', '02312345', 'ΑΦ 889655', '6901234567', '2310000568', 'ΘΕΣ/ΝΙΚΗ', '54627', '', 'Ε ΘΕΣ/ΝΙΚΗ', 'ΙΔΙΟΚΤΗΤΗΣ'),
(54, 'ΜΑΡΙΑ ΠΑΠΑΔΟΠΟΥΛΟΥ', 'ΣΒΩΛΟΥ 6', '100501001', 'ΑΝ 505050', '6932456789', '', 'ΘΕΣΣΑΛΟΝΙΚΗ', '54623', 'maria@gmail.com', 'ΚΑΛΑΜΑΡΙΑΣ', 'ΙΔΙΟΚΤΗΤΗΣ'),
(55, 'ΑΣΚΗΤΟΠΟΥΛΟΣ ΓΙΩΡΓΟΣ', 'ΝΙΚΟΛΑΟΥ ΠΑΡΑΣΚΕΥΑ 51', '112233445', 'ΑΟ 123456', '6949112233', '2315000000', 'ΣΥΚΙΕΣ', '56625', 'gaskit@mail.com', 'Ε ΘΕΣΣΑΛΟΝΙΚΗΣ', 'ΙΔΙΟΚΤΗΤΗΣ');

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `εταιρείες`
--

CREATE TABLE `εταιρείες` (
  `Κωδικός_Εταιρείας` int(10) NOT NULL,
  `Επωνυμία` varchar(80) NOT NULL,
  `Διεύθυνση` varchar(50) NOT NULL,
  `ΤΚ` varchar(5) NOT NULL,
  `Πόλη` varchar(25) NOT NULL,
  `ΑΦΜ` varchar(9) NOT NULL,
  `ΔΟΥ` varchar(25) NOT NULL,
  `Ιδιότητα` varchar(30) NOT NULL,
  `Σταθερό` varchar(10) NOT NULL,
  `Κινητό` varchar(10) NOT NULL,
  `email` varchar(50) NOT NULL,
  `Νόμιμος_Εκπρόσωπος` varchar(45) NOT NULL,
  `ΑΔΤ_Εκπροσώπου` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Άδειασμα δεδομένων του πίνακα `εταιρείες`
--

INSERT INTO `εταιρείες` (`Κωδικός_Εταιρείας`, `Επωνυμία`, `Διεύθυνση`, `ΤΚ`, `Πόλη`, `ΑΦΜ`, `ΔΟΥ`, `Ιδιότητα`, `Σταθερό`, `Κινητό`, `email`, `Νόμιμος_Εκπρόσωπος`, `ΑΔΤ_Εκπροσώπου`) VALUES
(10000, 'REVMA PLUS IKE', 'ΠΑΠΑΦΗ 175', '54352', 'ΘΕΣΣΑΛΟΝΙΚΗ', '997799778', 'Δ ΘΕΣΣΑΛΟΝΙΚΗΣ', 'Ενοικιαστής', '2310900444', '6900000000', 'revma@revma.gr', 'ΘΩΜΑΣ ΛΥΜΠΕΡΗΣ', 'ΑΑ 000000'),
(10002, 'ETAIRIA IKE', 'ΒΕΝΙΖΕΛΟΥ 10', '54630', 'ΘΕΣΣΑΛΟΝΙΚΗ', '997722364', 'ΘΕΣΣΑΛΟΝΙΚΗΣ', 'Ιδιοκτήτης', '2311223344', '6900112233', 'etairia@etairia.gr', 'ΠΑΠΑΔΟΠΟΥΛΟΣ ΓΕΩΡΓΙΟΣ', 'ΑΑ 112233'),
(10012, 'ouhg', 'oug', 'ogu', 'gou', '996633554', 'ojb', 'Ιδιοκτήτης', 'og', 'oug', 'oguoug', 'gou', 'vkhi'),
(10013, 'desa', 'agd', 'agd', 'agd', '996655221', 'SH', 'Ιδιοκτήτης', 'SWHR', 'HWRHRWH', 'WRHWR', 'HWRHWR', 'HRWHWR'),
(10014, 'gu', 'gou', 'gou', 'goug', '987456123', 'oug', 'Ιδιοκτήτης', 'oug', 'goug', 'uog', 'oug', 'oug'),
(10015, 'iyf', 'iyf', 'iyf', 'ify', '978456123', 'oug', 'Ιδιοκτήτης', 'oug', 'oug', 'ogu', 'guo', 'gou'),
(10016, 'ouh', 'h', 'h', 'h', '994455662', 'pij', 'Ιδιοκτήτης', 'pih', 'pih', 'pi', 'hph', 'ihpi'),
(10017, 'ou', 'oug', 'guo', 'guo', '963214587', 'oug', 'Ιδιοκτήτης', 'ogu', 'gou', 'guo', 'gou', 'guo'),
(10018, 'oph', 'hpi', 'hpi', 'hip', '095478921', 'poih', 'Ιδιοκτήτης', 'pih', 'pih', '', 'pgi', 'pig'),
(10019, 'COMMUNITY CENTER LIFE IKE', 'ΒΕΝΙΖΕΛΟΥ 19', '56625', 'ΣΥΚΙΕΣ', '998877665', 'Ε ΘΕΣΣΑΛΟΝΙΚΗ', 'ΙΔΙΟΚΤΗΤΗΣ', '2314002233', '6909090909', 'community@centerlife.gr', 'ΠΑΠΑΔΟΠΟΥΛΟΣ ΑΛΕΞΑΝΔΡΟΣ', 'ΑΚ 123456');

--
-- Ευρετήρια για άχρηστους πίνακες
--

--
-- Ευρετήρια για πίνακα `αιτήσεις`
--
ALTER TABLE `αιτήσεις`
  ADD PRIMARY KEY (`Κωδικός_Αίτησης`),
  ADD KEY `αιτήσεις_ibfk_1` (`Κωδικός_Επαφής`);

--
-- Ευρετήρια για πίνακα `επαφές`
--
ALTER TABLE `επαφές`
  ADD PRIMARY KEY (`Κωδικός_Επαφής`),
  ADD UNIQUE KEY `afm` (`ΑΦΜ`),
  ADD UNIQUE KEY `adt` (`ΑΔΤ`);

--
-- Ευρετήρια για πίνακα `εταιρείες`
--
ALTER TABLE `εταιρείες`
  ADD PRIMARY KEY (`Κωδικός_Εταιρείας`);

--
-- AUTO_INCREMENT για άχρηστους πίνακες
--

--
-- AUTO_INCREMENT για πίνακα `αιτήσεις`
--
ALTER TABLE `αιτήσεις`
  MODIFY `Κωδικός_Αίτησης` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=97;

--
-- AUTO_INCREMENT για πίνακα `επαφές`
--
ALTER TABLE `επαφές`
  MODIFY `Κωδικός_Επαφής` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=56;

--
-- AUTO_INCREMENT για πίνακα `εταιρείες`
--
ALTER TABLE `εταιρείες`
  MODIFY `Κωδικός_Εταιρείας` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10020;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
