package main

import (
	"github.com/LouisHatton/MUD-UI/internal/config"
	db_manager "github.com/LouisHatton/MUD-UI/internal/db/manager"
	dhcp_events "github.com/LouisHatton/MUD-UI/internal/dhcp/event"
	mud_manager "github.com/LouisHatton/MUD-UI/internal/mud/manager"
	osmud_reader "github.com/LouisHatton/MUD-UI/internal/osmud/reader"
	"github.com/caarlos0/env/v10"
	"go.uber.org/zap"
)

func main() {
	config := config.AppConfig{}
	if err := env.Parse(&config); err != nil {
		panic("attempting to parse config: " + err.Error())
	}

	logger, err := zap.NewDevelopment()
	if err != nil {
		panic("attempting to create a logger: " + err.Error())
	}

	dbManager := db_manager.NewDbManager(logger, config.DB.DbPath)
	db, err := dbManager.GetDatabase()
	if err != nil {
		logger.Fatal("error getting database", zap.Error(err))
	}
	defer db.Close()

	osMudReader := osmud_reader.New(logger, db)
	mudManager := mud_manager.New(logger, db)
	dhcpEventManager := dhcp_events.New(logger, config.EventsPath)

	server := NewServer(logger, osMudReader, mudManager, dhcpEventManager)
	server.Start(config.Port)
}
