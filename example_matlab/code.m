% Sample data
weeks = {'0-4 weeks', '5-8 weeks', '9-12 weeks', '13-16 weeks', '17-20 weeks', '21-26 weeks'};
n_values = [194, 65, 44, 31, 24, 7];

% Create bar chart
figure;
bar(n_values);

% Customize the chart
xlabel('Weeks');
ylabel( 'Number of episodes mastitis / women breastfeeding - weeks * 1000');
set(gca, 'XTickLabel', weeks);

% Add grid
grid on;

