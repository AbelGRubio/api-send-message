import uvicorn

from app import APP, LOGGER, API_PORT, API_IP

if __name__ == '__main__':
    LOGGER.debug("Starting...")
    uvicorn.run(
        APP,
        host=API_IP,
        port=API_PORT,
        reload=False,
    )
    LOGGER.debug("Ending.")
