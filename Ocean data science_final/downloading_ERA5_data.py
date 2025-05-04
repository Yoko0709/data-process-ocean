"""
Created on
@author: Ryota Tai
"""
import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type': 'reanalysis',
        'format': 'netcdf',
        'variable': [
            'significant_height_of_combined_wind_waves_and_swell',
            'mean_wave_direction', 
            'mean_wave_period',
            '10m_u_component_of_wind',
            '10m_v_component_of_wind',
            'mean_sea_level_pressure',
        ],
        'year': [
            '2015', '2016', '2017', '2018', '2019', 
            '2020', '2021', '2022', '2023', '2024',
        ],
        'month': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
        ],
        'day': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
            '13', '14', '15',
            '16', '17', '18',
            '19', '20', '21',
            '22', '23', '24',
            '25', '26', '27',
            '28', '29', '30',
            '31',
        ],
        'time': [
            '12:00', 
        ],
        'area': [
            20, 120,
            40, 130,

        ],
    },
    'ocean_atmos_2015-2024-every-day-1200.nc')
