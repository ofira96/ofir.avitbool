
function create_contact_list(users){
    console.log(users);
    const curr_main = document.querySelector("main");
    for(let user of users){
        const section =document.createElmennt("section");
        section.innerHTML = `
        <img src="${user.avatar}" alt="Profile Picture"/>
        <div>
            <span>${user.first_name} ${user.last_name}</span>
            <br>
            <a herf="mailto:${user.email}">Send Email</a>
        </div>
        `;

        curr_main.appendChild(section);
    }
}
