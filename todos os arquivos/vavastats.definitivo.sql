
CREATE DATABASE IF NOT EXISTS `VAVASTATS` DEFAULT CHARACTER SET utf8mb3 ;
USE `VAVASTATS` ;


-- Criação da tabela TBL_AGENTS
CREATE TABLE TBL_AGENTS (
    AgentID INT AUTO_INCREMENT PRIMARY KEY,
    AGENT VARCHAR(255) NOT NULL,
    PICK_RATE DOUBLE NOT NULL,
    ACS DOUBLE NOT NULL,
    KD DOUBLE NOT NULL
);

-- Criação da tabela TBL_PLAYERS
CREATE TABLE TBL_PLAYERS (
    PlayerID INT AUTO_INCREMENT PRIMARY KEY,
    PLAYER VARCHAR(255) NOT NULL,
    COUNTRY VARCHAR(255) NOT NULL,
    TEAM VARCHAR(255), -- Chave estrangeira será adicionada posteriormente
    ACS DOUBLE NOT NULL,
    KD DOUBLE NOT NULL
);

-- Criação da tabela TBL_MAPS
CREATE TABLE TBL_MAPS (
    MapID INT AUTO_INCREMENT PRIMARY KEY,
    MAP VARCHAR(255) NOT NULL,
    PLAYED INT NOT NULL
);

-- Criação da tabela TBL_TEAMS
CREATE TABLE TBL_TEAMS (
    TeamID INT AUTO_INCREMENT PRIMARY KEY,
    TEAM VARCHAR(255) NOT NULL,
    COUNTRY VARCHAR(255) NOT NULL
);

-- Tabela de associação entre TBL_PLAYERS e TBL_AGENTS
CREATE TABLE TBL_PLAYERS_AGENTS (
    PlayerID INT,
    AgentID INT,
    PRIMARY KEY (PlayerID, AgentID),
    FOREIGN KEY (PlayerID) REFERENCES TBL_PLAYERS(PlayerID),
    FOREIGN KEY (AgentID) REFERENCES TBL_AGENTS(AgentID)
);

-- Tabela de associação entre TBL_TEAMS e TBL_MAPS
CREATE TABLE TBL_TEAMS_MAPS (
    TeamID INT,
    MapID INT,
    PRIMARY KEY (TeamID, MapID),
    FOREIGN KEY (TeamID) REFERENCES TBL_TEAMS(TeamID),
    FOREIGN KEY (MapID) REFERENCES TBL_MAPS(MapID)
);

-- Tabela de associação entre TBL_AGENTS e TBL_MAPS
CREATE TABLE TBL_AGENTS_MAPS (
    AgentID INT,
    MapID INT,
    PRIMARY KEY (AgentID, MapID),
    FOREIGN KEY (AgentID) REFERENCES TBL_AGENTS(AgentID),
    FOREIGN KEY (MapID) REFERENCES TBL_MAPS(MapID)
);

ALTER TABLE tbl_agents MODIFY PICK_RATE VARCHAR(255);


select * from tbl_agents;