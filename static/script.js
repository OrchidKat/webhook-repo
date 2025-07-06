function fetchEvents() {
  fetch('/events')
    .then(res => res.json())
    .then(data => {
      const container = document.getElementById('events-container');
      container.innerHTML = '';
      data.forEach(ev => {
        let msg = "";
        const date = new Date(ev.timestamp).toUTCString();
        if (ev.event_type === "push") {
          msg = `${ev.author} pushed to ${ev.to_branch} on ${date}`;
        } else if (ev.event_type === "pull_request") {
          msg = `${ev.author} submitted a pull request from ${ev.from_branch} to ${ev.to_branch} on ${date}`;
        } else if (ev.event_type === "merge") {
          msg = `${ev.author} merged branch ${ev.from_branch} to ${ev.to_branch} on ${date}`;
        }
        const p = document.createElement('p');
        p.innerText = msg;
        container.appendChild(p);
      });
    });
}

fetchEvents();
setInterval(fetchEvents, 15000);
