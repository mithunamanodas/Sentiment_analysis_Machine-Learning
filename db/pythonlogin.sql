-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 27, 2023 at 12:51 PM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 7.4.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pythonlogin`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts`
--

CREATE TABLE `accounts` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `accounts`
--

INSERT INTO `accounts` (`id`, `username`, `password`, `email`) VALUES
(1, 'test', 'test', 'test@test.com'),
(2, 'akshay', '1234', 'ak@123gmail.com'),
(3, 'akshaykrish', '12345', 'akshay264@gmil.com'),
(4, 'demo', '1234', 'demo@gmail.com'),
(5, 'demo', '12345', 'demo@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `sentiment`
--

CREATE TABLE `sentiment` (
  `id` int(11) NOT NULL,
  `comment` varchar(500) CHARACTER SET utf8 NOT NULL,
  `sentiment` varchar(500) CHARACTER SET utf8 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sentiment`
--

INSERT INTO `sentiment` (`id`, `comment`, `sentiment`) VALUES
(1, 'good', 'positive'),
(2, 'bad', 'negative'),
(3, 'not bad', 'positive'),
(4, 'wonderful', 'good'),
(5, 'too bad', 'negative'),
(6, 'wow', 'positive'),
(7, 'nice', 'positive'),
(8, 'superrr', 'positive'),
(9, 'review', 'sentiment'),
(11, 'wonderfull movie', 'Neutral'),
(12, 'super movie', 'Positive'),
(13, 'nice movie', 'Positive'),
(14, 'nice movie', 'Positive'),
(15, 'nice movie and good', 'Positive'),
(16, 'nice movie and good', 'Positive'),
(17, 'nice movie and good', 'Positive'),
(18, 'good movie', 'Positive');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accounts`
--
ALTER TABLE `accounts`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sentiment`
--
ALTER TABLE `sentiment`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accounts`
--
ALTER TABLE `accounts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `sentiment`
--
ALTER TABLE `sentiment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
