import React from "react";

// Import React Table
import ReactTable from "react-table";
import "react-table/react-table.css";

import namor from "namor";
import moment from "moment";

const range = len => {
    const arr = [];
    for (let i = 0; i < len; i++) {
        arr.push(i);
    }
    return arr;
};

const newPerson = () => {
    return {
        flight: namor.generate({ words: 2, numbers: 0 }),
        time: moment.unix(
            Math.floor(Math.random() * 1000000000)
        ),
        age: Math.floor(Math.random() * 30),
    };
};

function makeData(len = 5553) {
    return range(len).map(d => {
        let p = newPerson();
        return p;
    });
}

class CardContentTable extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            data: makeData()
        };
    }

    render() {
        return (
            <ReactTable
                data={this.state.data}
                columns={[
                    {
                        Header: "Capture",
                        columns: [
                            {
                                Header: "Time",
                                id: "time",
                                accessor: d => d.time.toISOString(),
                            },
                            {
                                Header: "Flight",
                                id: "flight",
                                accessor: d => d.flight
                            }
                        ]
                    },
                    {
                        Header: "Information",
                        columns: [
                            {
                                Header: "Age",
                                accessor: "age"
                            }
                        ]
                    }
                ]}
                defaultPageSize={15}
                className="-striped -highlight"
                getTrProps={(state, rowInfo) => {
                    return {
                      onClick: (e) => {
                        this.props.store.dispatch({
                            type: 'change-selection',
                            action: rowInfo.original,
                        });
                      }
                    }
                  }
                }
            />
        );
    }
}

export default CardContentTable;
