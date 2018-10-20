import React from "react";

// Import React Table
import ReactTable from "react-table";
import "react-table/react-table.css";

import $ from 'jquery';

import moment from "moment";

class CardContentTable extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            data: [],
        }
        this.props.objectStore.subscribe(() => this.setState({
            data: this.props.objectStore.getState().filteredObjects,
        }));
    }

    componentDidMount() {
        $(".ReactTable").height($(".ReactTable").parent().height());
        // // temporary fix
        // $(".card-footer").height($(".pagination-bottom").height());
    }

    render() {
        // temporary fix
        // $(".card-footer").height($(".pagination-bottom").height());
        return (
            <ReactTable
                data={this.state.data}
                columns={[
                    {
                        Header: "Capture",
                        columns: [
                            {
                                Header: "Type",
                                accessor: "object_name",
                            },
                            {
                                Header: "Flight",
                                id: "flight",
                                accessor: d => d.flight.$oid,
                            },
                            {
                                Header: "Point",
                                accessor: d => d.point.coordinates[0] + " " + d.point.coordinates[1],
                                id: "point",
                            },                            
                            {
                                Header: "Time",
                                accessor: d => moment.unix(d.time.$date).toISOString(),
                                id: "time",
                            },
                        ]
                    },
                ]}
                defaultPageSize={this.props.numberOfRows}
                className="-striped -highlight"
                getTrProps={(state, rowInfo) => {
                    return {
                      onClick: (e) => {
                        // this.props.store.dispatch({
                        //     type: 'change-selection',
                        //     action: rowInfo.original,
                        // });
                      }
                    }
                  }
                }
            />
        );
    }
}

export default CardContentTable;
