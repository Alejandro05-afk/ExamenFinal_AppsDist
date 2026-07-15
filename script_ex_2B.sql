CREATE DATABASE IF NOT EXISTS examenad;
USE examenad;

CREATE TABLE IF NOT EXISTS redes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(15) NOT NULL,
    accion VARCHAR(10) NOT NULL,
    fecha VARCHAR(20) NOT NULL,
    hora VARCHAR(20) NOT NULL,
    short VARCHAR(20) NOT NULL
);

TRUNCATE TABLE redes;

INSERT INTO redes (usuario, accion, fecha, hora, short) VALUES
('Diego','view','7/8/2026','6:01','video8'),
('Sofia','shared','7/9/2026','13:57','video13'),
('Ximena','view','7/25/2026','23:22','video15'),
('Moises','like','7/21/2026','19:50','video14'),
('Marta','view','7/7/2026','12:07','video7'),
('Moises','comment','7/30/2026','18:29','video1'),
('Moises','shared','7/12/2026','8:07','video13'),
('Diego','comment','7/23/2026','7:49','video12'),
('Sofia','like','7/5/2026','23:57','video13'),
('Marta','like','7/27/2026','17:42','video4'),
('Ximena','shared','7/6/2026','16:22','video3'),
('Jorge','comment','7/8/2026','11:50','video2'),
('Ximena','comment','7/23/2026','16:47','video6'),
('Moises','comment','7/24/2026','1:25','video2'),
('Ximena','shared','7/3/2026','10:20','video1'),
('Rocio','like','7/9/2026','8:45','video7'),
('Moises','like','7/3/2026','23:43','video1'),
('Moises','like','7/9/2026','21:49','video7'),
('Moises','comment','7/24/2026','12:09','video7'),
('Diego','like','7/4/2026','12:56','video11'),
('Julia','like','7/15/2026','10:41','video8'),
('Ximena','like','7/10/2026','13:58','video4'),
('Ximena','view','7/4/2026','12:31','video1'),
('Ximena','comment','7/10/2026','11:55','video9'),
('Moises','shared','7/1/2026','9:27','video11'),
('Luis','comment','7/25/2026','5:07','video2'),
('Marta','like','7/1/2026','1:40','video3'),
('Sofia','shared','7/17/2026','2:14','video4'),
('Moises','like','7/25/2026','19:52','video8'),
('Marta','comment','7/16/2026','2:40','video14');
