from selfapi import app
import create_test_data

create_test_data.clean()
create_test_data.init()

app.run()