from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A list to store event data (replace with a database in a production setting)
events = []

class Event:
    def __init__(self, name, date, time, description, organizer):
        self.name = name
        self.date = date
        self.time = time
        self.description = description
        self.organizer = organizer

@app.route('/')
def index():
    return render_template('index.html', events=events)

@app.route('/add_event', methods=['POST'])
def add_event():
    name = request.form['name']
    date = request.form['date']
    time = request.form['time']
    description = request.form['description']
    organizer = request.form['organizer']
    
    event = Event(name, date, time, description, organizer)
    events.append(event.__dict__)
    
    return redirect(url_for('index'))

@app.route('/edit_event/<int:event_index>', methods=['GET', 'POST'])
def edit_event(event_index):
    if request.method == 'POST':
        try:
            # Update the event with the new data from the form
            events[event_index - 1]['name'] = request.form['name']
            events[event_index - 1]['date'] = request.form['date']
            events[event_index - 1]['time'] = request.form['time']
            events[event_index - 1]['description'] = request.form['description']
            events[event_index - 1]['organizer'] = request.form['organizer']
        
            return redirect(url_for('index'))
        except Exception as e:
            # Handle the exception, e.g., log it or return an error page
            return f"An error occurred: {str(e)}"
    
    return render_template('edit_event.html', event=events[event_index - 1], event_index=event_index)

@app.route('/delete_event/<int:event_index>')
def delete_event(event_index):
    if 1 <= event_index <= len(events):
        del events[event_index - 1]
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
