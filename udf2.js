function process(inJson) {
    // Assuming inJson is the CSV row as a string, no need to use JSON.parse on it
    const playerData = inJson.split(',');
  
    // Create a structured object based on the CSV row data
    const playerDetails = {
      player_id: parseInt(playerData[0].trim(), 10),
      player_name: playerData[1].trim(),
      country: playerData[2].trim()
    };
  
    // Return the structured object as a JSON string
    return JSON.stringify(playerDetails);
  }
  
  
