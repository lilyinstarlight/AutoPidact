library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity AutoPidact is
	port(
		CLOCK_50_B5B : in    std_logic;
		GPIO         : inout std_logic_vector(35 downto 0)
	);
end entity AutoPidact;

architecture RTL of AutoPidact is
	signal spi_busy : std_logic;
	signal spi_rrdy  : std_logic;
	signal spi_rreq  : std_logic;
	signal spi_rdata : std_logic_vector(31 downto 0);

	signal mtr0_pwm : unsigned(6 downto 0);
	signal mtr0     : std_logic;
	signal mtr1_pwm : unsigned(6 downto 0);
	signal mtr1     : std_logic;
	signal mtr2_pwm : unsigned(6 downto 0);
	signal mtr2     : std_logic;
	signal mtr3_pwm : unsigned(6 downto 0);
	signal mtr3     : std_logic;
begin
	spi:  entity work.spi_slave
	      generic map(d_width => 32)
	      port map(sclk => GPIO(11), mosi => GPIO(12), miso => GPIO(13), ss_n => GPIO(14), busy => spi_busy, reset_n => '1', tx_load_en => '0', tx_load_data => "00000000000000000000000000000000", rx_req => spi_rreq, rx_data => spi_rdata, trdy => open, rrdy => spi_rrdy, roe => open, st_load_en => '0', st_load_trdy => '0', st_load_rrdy => '0', st_load_roe => '0');

	spi_rreq <= spi_rrdy;

	mtr0_pwm <= unsigned(spi_rdata(6 downto 0));
	mtr1_pwm <= unsigned(spi_rdata(14 downto 8));
	mtr2_pwm <= unsigned(spi_rdata(22 downto 16));
	mtr3_pwm <= unsigned(spi_rdata(30 downto 24));

	pwm0: entity work.PWM
	      generic map(cycle => 50000, width => 127)
	      port map(clk => CLOCK_50_B5B, pwm => mtr0_pwm, q => mtr0);

	pwm1: entity work.PWM
	      generic map(cycle => 50000, width => 127)
	      port map(clk => CLOCK_50_B5B, pwm => mtr1_pwm, q => mtr1);

	pwm2: entity work.PWM
	      generic map(cycle => 50000, width => 127)
	      port map(clk => CLOCK_50_B5B, pwm => mtr2_pwm, q => mtr2);

	pwm3: entity work.PWM
	      generic map(cycle => 50000, width => 127)
	      port map(clk => CLOCK_50_B5B, pwm => mtr3_pwm, q => mtr3);

	process(spi_rdata)
	begin
		if (spi_rdata(7) = '0') then
			GPIO(3) <= mtr0;
			GPIO(4) <= '1';
		else
			GPIO(3) <= '1';
			GPIO(4) <= mtr0;
		end if;

		if (spi_rdata(15) = '0') then
			GPIO(5) <= mtr1;
			GPIO(6) <= '1';
		else
			GPIO(5) <= '1';
			GPIO(6) <= mtr1;
		end if;

		if (spi_rdata(23) = '0') then
			GPIO(7) <= mtr2;
			GPIO(8) <= '1';
		else
			GPIO(7) <= '1';
			GPIO(8) <= mtr2;
		end if;

		if (spi_rdata(31) = '0') then
			GPIO(9) <= mtr3;
			GPIO(10) <= '1';
		else
			GPIO(9) <= '1';
			GPIO(10) <= mtr3;
		end if;
	end process;
end RTL;