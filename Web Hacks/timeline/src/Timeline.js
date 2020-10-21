import React from 'react';
import Chart from "react-google-charts";

function Timeline(props) {
  if (props.data.length === 1) {
    return (
      <p className='text-center text-muted mt-5'>Enter An Item</p>
    );
  } else {
    // See https://react-google-charts.com/timeline-chart for documentation
    return (
      <Chart
        width={'100%'}
        height={'200px'}
        chartType="Timeline"
        loader={<div>Loading Chart</div>}
        data={props.data}
        rootProps={{ 'data-testid': '3' }}
      />
    );
  }
}

export default Timeline;
