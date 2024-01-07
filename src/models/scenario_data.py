from helpers.database import get_mysql_connection as get_db
from helpers.result import OperationResult as Result


class ScenarioData:
    def __init__(self, scenario_id, in_progress=True, id=None):
        self.id = id
        self.scenario_id = scenario_id
        self.in_progress = in_progress
        
        
def create_scenario_data(scenario_id: int) -> Result:
    db = get_db()
    cursor = db.cursor()
    cursor.execute('INSERT INTO Scenario_Data (scenario_id, in_progress) VALUES (%s, %s)', (scenario_id, True))
    data_id = cursor.lastrowid
    db.commit()
    cursor.close()
    db.close()
    return Result(True, "Scenario data created successfully", {"data_id": data_id})
    
    
def get_scenario_data(scenario_id: int) -> Result:
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Scenario_Data WHERE scenario_id like '%s'" % scenario_id)
    for id, scenario_id, in_progress in cursor:
        cursor.close()
        db.close()
        data = ScenarioData(scenario_id, in_progress, id)
        return Result(True, "Scenario data found", {'data': data})
    return Result(False, 'Scenario data is not present!')
    
    
def set_scenario_data_in_progress(scenario_id: int, in_progress: bool) -> Result:
    db = get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE Scenario_Data SET in_progress = %s WHERE scenario_id = %s", (in_progress, scenario_id))
    db.commit()
    cursor.close()
    db.close()
    return Result(True, "Scenario data updated successfully")