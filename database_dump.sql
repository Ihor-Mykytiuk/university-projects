--
-- PostgreSQL database dump
--

-- Dumped from database version 15.5
-- Dumped by pg_dump version 15.5

-- Started on 2024-01-07 01:27:18

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 214 (class 1259 OID 16403)
-- Name: buildings; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.buildings (
    buildingid integer NOT NULL,
    buildingname character varying(128) NOT NULL,
    address character varying(128) NOT NULL
);


ALTER TABLE public.buildings OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 16408)
-- Name: classrooms; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.classrooms (
    classroomid integer NOT NULL,
    roomnumber integer NOT NULL,
    buildingid integer NOT NULL
);


ALTER TABLE public.classrooms OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 16418)
-- Name: computercharacteristics; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.computercharacteristics (
    characteristicid integer NOT NULL,
    memory character varying(16) NOT NULL,
    ram character varying(16) NOT NULL,
    cpu character varying(32) NOT NULL,
    videocard character varying(32) NOT NULL
);


ALTER TABLE public.computercharacteristics OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16423)
-- Name: computers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.computers (
    computerid integer NOT NULL,
    serialnumber character varying(16) NOT NULL,
    characteristicid integer NOT NULL,
    purchasedate date,
    roomid integer NOT NULL
);


ALTER TABLE public.computers OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16448)
-- Name: devicetypes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.devicetypes (
    devicetypeid integer NOT NULL,
    typename character varying(32) NOT NULL,
    description text NOT NULL
);


ALTER TABLE public.devicetypes OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 16455)
-- Name: networkequipment; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.networkequipment (
    networkequipmentid integer NOT NULL,
    serialnumber character varying(16) NOT NULL,
    buildingid integer NOT NULL,
    devicetypeid integer NOT NULL,
    manufacturer character varying(16) NOT NULL,
    model character varying(32) NOT NULL
);


ALTER TABLE public.networkequipment OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 16438)
-- Name: peripherals; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.peripherals (
    peripheralid character varying(3) NOT NULL,
    type character varying(16) NOT NULL,
    brand character varying(16) NOT NULL,
    model character varying(32) NOT NULL,
    computerid integer
);


ALTER TABLE public.peripherals OWNER TO postgres;

--
-- TOC entry 3358 (class 0 OID 16403)
-- Dependencies: 214
-- Data for Name: buildings; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.buildings VALUES (1, 'Центральний корпус', 'вул. Шевченка, 57');
INSERT INTO public.buildings VALUES (2, 'Гуманітарний корпус', 'вул. Шевченка, 57');
INSERT INTO public.buildings VALUES (3, 'Навчально-науковий юридичний інститут', 'вул. Шевченка, 44а');


--
-- TOC entry 3359 (class 0 OID 16408)
-- Dependencies: 215
-- Data for Name: classrooms; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.classrooms VALUES (11, 309, 1);
INSERT INTO public.classrooms VALUES (12, 201, 2);
INSERT INTO public.classrooms VALUES (13, 320, 1);
INSERT INTO public.classrooms VALUES (14, 105, 3);
INSERT INTO public.classrooms VALUES (15, 306, 1);


--
-- TOC entry 3360 (class 0 OID 16418)
-- Dependencies: 216
-- Data for Name: computercharacteristics; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.computercharacteristics VALUES (101, '512GB SSD', '16GB', 'Intel Core i7', 'NVIDIA GeForce RTX 3070');
INSERT INTO public.computercharacteristics VALUES (102, '1TB HDD', '8GB', 'AMD Ryzen 5', 'NVIDIA GeForce GTX 1660 Ti');
INSERT INTO public.computercharacteristics VALUES (103, '256GB SSD', '8GB', 'Intel Core i9', 'AMD Radeon RX 6800');
INSERT INTO public.computercharacteristics VALUES (104, '2TB HDD', '16GB', 'AMD Ryzen 7', 'NVIDIA GeForce RTX 3060');
INSERT INTO public.computercharacteristics VALUES (105, '512GB SSD', '8GB', 'Intel Core i5', 'AMD Radeon RX 6700 XT');
INSERT INTO public.computercharacteristics VALUES (106, '1TB SSD', '8GB', 'AMD Ryzen 9', 'NVIDIA GeForce RTX 3080');
INSERT INTO public.computercharacteristics VALUES (107, '3TB HDD', '16GB', 'Intel Core i9', 'AMD Radeon RX 6900 XT');


--
-- TOC entry 3361 (class 0 OID 16423)
-- Dependencies: 217
-- Data for Name: computers; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.computers VALUES (1, 'ABC123', 101, '2021-09-15', 11);
INSERT INTO public.computers VALUES (2, 'DEF456', 102, '2021-10-20', 11);
INSERT INTO public.computers VALUES (3, 'GHI789', 103, '2021-11-25', 13);
INSERT INTO public.computers VALUES (4, 'JKL012', 104, '2021-12-30', 13);
INSERT INTO public.computers VALUES (5, 'MNO345', 105, '2020-01-05', 15);
INSERT INTO public.computers VALUES (6, 'PQR678', 106, '2020-02-10', 11);
INSERT INTO public.computers VALUES (7, 'STU901', 107, '2019-03-15', 12);
INSERT INTO public.computers VALUES (8, 'VWX234', 101, '2022-04-20', 13);
INSERT INTO public.computers VALUES (9, 'YZA567', 102, '2022-05-25', 14);
INSERT INTO public.computers VALUES (10, 'BCD890', 103, '2018-06-30', 15);
INSERT INTO public.computers VALUES (11, 'EFG123', 104, '2021-08-05', 11);
INSERT INTO public.computers VALUES (12, 'HIJ456', 105, '2019-09-10', 12);
INSERT INTO public.computers VALUES (13, 'KLM789', 106, '2022-10-15', 13);
INSERT INTO public.computers VALUES (14, 'NOP012', 107, '2022-11-20', 11);
INSERT INTO public.computers VALUES (15, 'QRS345', 101, '2022-12-25', 15);


--
-- TOC entry 3363 (class 0 OID 16448)
-- Dependencies: 219
-- Data for Name: devicetypes; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.devicetypes VALUES (2001, 'Router', 'Network device that forwards data between computer networks');
INSERT INTO public.devicetypes VALUES (2002, 'Switch', 'Network device that connects devices within a local area network (LAN)');
INSERT INTO public.devicetypes VALUES (2003, 'Access Point', 'Device that allows a Wi-Fi device to connect to a wired network');
INSERT INTO public.devicetypes VALUES (2004, 'Retranslator', 'Device that reroutes network traffic to enhance performance and security');


--
-- TOC entry 3364 (class 0 OID 16455)
-- Dependencies: 220
-- Data for Name: networkequipment; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.networkequipment VALUES (3001, 'ABC123', 1, 2004, 'TP-Link', 'RE305');
INSERT INTO public.networkequipment VALUES (3002, 'DEF456', 2, 2002, 'Netgear', '500');
INSERT INTO public.networkequipment VALUES (3003, 'GHI789', 1, 2003, 'TP-Link', 'A200');
INSERT INTO public.networkequipment VALUES (3004, 'JKL012', 3, 2004, 'Tenda', 'X3');
INSERT INTO public.networkequipment VALUES (3005, 'MNO345', 2, 2001, 'Cisco', '2000');
INSERT INTO public.networkequipment VALUES (3006, 'PQR678', 1, 2002, 'D-Link', 'S300');
INSERT INTO public.networkequipment VALUES (3007, 'STU901', 3, 2003, 'Linksys', 'B300');
INSERT INTO public.networkequipment VALUES (3008, 'VWX234', 2, 2001, 'Mercusys', 'ME20');
INSERT INTO public.networkequipment VALUES (3009, 'XYZ567', 1, 2001, 'Netis', 'N100');
INSERT INTO public.networkequipment VALUES (3010, 'ABC890', 2, 2002, 'Tenda', 'S200');
INSERT INTO public.networkequipment VALUES (3011, 'DEF111', 3, 2003, 'Mercusys', 'M300');


--
-- TOC entry 3362 (class 0 OID 16438)
-- Dependencies: 218
-- Data for Name: peripherals; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.peripherals VALUES ('OSA', 'Mouse', 'Basic', 'Basic Mouse', 1);
INSERT INTO public.peripherals VALUES ('OSB', 'Keyboard', 'Basic', 'Basic Keyboard', 1);
INSERT INTO public.peripherals VALUES ('OSC', 'Mouse', 'Basic', 'Basic Mouse', 2);
INSERT INTO public.peripherals VALUES ('OSD', 'Keyboard', 'Basic', 'Basic Keyboard', 2);
INSERT INTO public.peripherals VALUES ('OSE', 'Mouse', 'Basic', 'Basic Mouse', 3);
INSERT INTO public.peripherals VALUES ('OSF', 'Keyboard', 'Basic', 'Basic Keyboard', 3);
INSERT INTO public.peripherals VALUES ('OSG', 'Mouse', 'HP', 'Basic Mouse', 4);
INSERT INTO public.peripherals VALUES ('OSH', 'Keyboard', 'Logitech', 'Standard Keyboard', 4);
INSERT INTO public.peripherals VALUES ('OSI', 'Mouse', 'Logitech', 'Basic Mouse', 5);
INSERT INTO public.peripherals VALUES ('OSJ', 'Keyboard', 'Microsoft', 'Basic Keyboard', 5);
INSERT INTO public.peripherals VALUES ('OSK', 'Mouse', 'Dell', 'Simple Mouse', 6);
INSERT INTO public.peripherals VALUES ('OSL', 'Keyboard', 'Dell', 'Standard Keyboard', 6);
INSERT INTO public.peripherals VALUES ('OSM', 'Mouse', 'HP', 'Basic Mouse', 7);
INSERT INTO public.peripherals VALUES ('OSN', 'Keyboard', 'Logitech', 'Standard Keyboard', 7);
INSERT INTO public.peripherals VALUES ('OSO', 'Mouse', 'Logitech', 'Basic Mouse', 8);
INSERT INTO public.peripherals VALUES ('OSP', 'Keyboard', 'Dell', 'Basic Keyboard', 8);
INSERT INTO public.peripherals VALUES ('OSQ', 'Mouse', 'SteelSeries', 'Basic Mouse', 9);
INSERT INTO public.peripherals VALUES ('OSR', 'Keyboard', 'Ducky', 'Basic Keyboard', 9);
INSERT INTO public.peripherals VALUES ('OSS', 'Mouse', 'Logitech', 'Basic Mouse', 10);
INSERT INTO public.peripherals VALUES ('OST', 'Keyboard', 'Razer', 'Basic Keyboard', 10);
INSERT INTO public.peripherals VALUES ('OSU', 'Mouse', 'Corsair', 'Basic Mouse', 11);
INSERT INTO public.peripherals VALUES ('OSV', 'Keyboard', 'SteelSeries', 'Basic Keyboard', 11);
INSERT INTO public.peripherals VALUES ('OSW', 'Mouse', 'Logitech', 'Basic Mouse', 12);
INSERT INTO public.peripherals VALUES ('OSX', 'Keyboard', 'HyperX', 'Basic Keyboard', 12);
INSERT INTO public.peripherals VALUES ('OSY', 'Mouse', 'Razer', 'Basic Mouse', 13);
INSERT INTO public.peripherals VALUES ('OSZ', 'Keyboard', 'Corsair', 'Basic Keyboard', 13);
INSERT INTO public.peripherals VALUES ('OS1', 'Mouse', 'Logitech', 'Basic Mouse', 14);
INSERT INTO public.peripherals VALUES ('OS2', 'Keyboard', 'Ducky', 'Basic Keyboard', 14);
INSERT INTO public.peripherals VALUES ('OS3', 'Mouse', 'SteelSeries', 'Basic Mouse', 15);
INSERT INTO public.peripherals VALUES ('OS4', 'Keyboard', 'Logitech', 'Basic Keyboard', 15);
INSERT INTO public.peripherals VALUES ('OS5', 'Printer', 'Epson', 'Laser Printer', 4);
INSERT INTO public.peripherals VALUES ('OS6', 'Printer', 'Canon', 'Inkjet Printer', 5);
INSERT INTO public.peripherals VALUES ('OS7', 'Printer', 'Brother', 'Multifunction Printer', 6);
INSERT INTO public.peripherals VALUES ('OS8', 'Printer', 'Samsung', 'Wireless Printer', 7);
INSERT INTO public.peripherals VALUES ('OS9', 'Printer', 'Xerox', 'Color Laser Printer', 8);


--
-- TOC entry 3197 (class 2606 OID 16407)
-- Name: buildings buildings_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.buildings
    ADD CONSTRAINT buildings_pkey PRIMARY KEY (buildingid);


--
-- TOC entry 3199 (class 2606 OID 16412)
-- Name: classrooms classrooms_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classrooms
    ADD CONSTRAINT classrooms_pkey PRIMARY KEY (classroomid);


--
-- TOC entry 3201 (class 2606 OID 16422)
-- Name: computercharacteristics computercharacteristics_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.computercharacteristics
    ADD CONSTRAINT computercharacteristics_pkey PRIMARY KEY (characteristicid);


--
-- TOC entry 3203 (class 2606 OID 16427)
-- Name: computers computers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.computers
    ADD CONSTRAINT computers_pkey PRIMARY KEY (computerid);


--
-- TOC entry 3207 (class 2606 OID 16454)
-- Name: devicetypes devicetypes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.devicetypes
    ADD CONSTRAINT devicetypes_pkey PRIMARY KEY (devicetypeid);


--
-- TOC entry 3209 (class 2606 OID 16459)
-- Name: networkequipment networkequipment_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.networkequipment
    ADD CONSTRAINT networkequipment_pkey PRIMARY KEY (networkequipmentid);


--
-- TOC entry 3205 (class 2606 OID 16442)
-- Name: peripherals peripherals_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.peripherals
    ADD CONSTRAINT peripherals_pkey PRIMARY KEY (peripheralid);


--
-- TOC entry 3210 (class 2606 OID 16413)
-- Name: classrooms classrooms_buildingid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classrooms
    ADD CONSTRAINT classrooms_buildingid_fkey FOREIGN KEY (buildingid) REFERENCES public.buildings(buildingid);


--
-- TOC entry 3211 (class 2606 OID 16428)
-- Name: computers computers_characteristicid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.computers
    ADD CONSTRAINT computers_characteristicid_fkey FOREIGN KEY (characteristicid) REFERENCES public.computercharacteristics(characteristicid);


--
-- TOC entry 3212 (class 2606 OID 16433)
-- Name: computers computers_roomid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.computers
    ADD CONSTRAINT computers_roomid_fkey FOREIGN KEY (roomid) REFERENCES public.classrooms(classroomid);


--
-- TOC entry 3214 (class 2606 OID 16460)
-- Name: networkequipment networkequipment_buildingid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.networkequipment
    ADD CONSTRAINT networkequipment_buildingid_fkey FOREIGN KEY (buildingid) REFERENCES public.buildings(buildingid);


--
-- TOC entry 3215 (class 2606 OID 16465)
-- Name: networkequipment networkequipment_devicetypeid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.networkequipment
    ADD CONSTRAINT networkequipment_devicetypeid_fkey FOREIGN KEY (devicetypeid) REFERENCES public.devicetypes(devicetypeid);


--
-- TOC entry 3213 (class 2606 OID 16443)
-- Name: peripherals peripherals_computerid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.peripherals
    ADD CONSTRAINT peripherals_computerid_fkey FOREIGN KEY (computerid) REFERENCES public.computers(computerid);


-- Completed on 2024-01-07 01:27:19

--
-- PostgreSQL database dump complete
--

