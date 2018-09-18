import "./style.css";
import React from "react";

// sidebar list component
import SidebarList from "../sidebarList";

class Sidebar extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            sidebarLists: []
        }
        this.store = props.store;
        this.content = props.content;

        if (props.content == "flights")
        {
            this.state.sidebarLists = [
                {
                    title: "Flights",
                    list: [
                        "Cras justo odio",
                        "Dapibus ac facilisis in",
                        "Morbi leo risus",
                        "Cras justo odio",
                        "Dapibus ac facilisis in",
                        "Morbi leo risus",
                        "Cras justo odio",
                        "Dapibus ac facilisis in",
                        "Morbi leo risus",
                    ]
                }
            ]
        }
        else if (props.content == "flightData")
        {
            this.state.sidebarLists = [
                {
                    title: "Sensors",
                    list: [
                        "NIRVSS long wave",
                        "NIRVSS short wave",
                        "Relative humidity",
                        "Temperature",
                    ]
                },
                {
                    title: "Photos",
                    list: [...Array(5).keys()].map(
                        (i) => (`Photo number ${i + 1}`)
                    )
                },
                {
                    title: "Notes",
                    list: [
                        "Cras justo odio",
                        "Dapibus ac facilisis in",
                        "Morbi leo risus",
                        "Porta ac consectetur ac",
                    ]
                },
            ]
        }
    }

    render() {
        let array = this.state.sidebarLists.map(
            (r, id) => (
                <div key={id}>
                    <h5>{r.title}</h5>
                    <SidebarList 
                        list={r.list} 
                        store={this.store}
                        content={this.content}
                    />
                </div>
            )
        )

        return (
            <div className="sidebar">
                {array}
            </div>
        );
    }
}

export default Sidebar;
