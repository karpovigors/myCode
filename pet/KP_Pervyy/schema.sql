--
-- PostgreSQL database dump
--

\restrict DLdoguJbcXkH7ppZpq6LtXU0eeHdZLHV4BFYZ8pgseegFHBrAtwcuwhNTlDNdvK

-- Dumped from database version 15.15 (Homebrew)
-- Dumped by pg_dump version 15.15 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: neighbors; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.neighbors (
    neighbor_id bigint NOT NULL,
    last_name text,
    first_name text NOT NULL,
    middle_name text,
    phone text DEFAULT ''::text NOT NULL,
    note text DEFAULT ''::text NOT NULL,
    birth_date date,
    CONSTRAINT neighbors_phone_check CHECK (((phone = ''::text) OR (phone ~ '^\+[1-9][0-9]{7,14}$'::text)))
);


--
-- Name: neighbors_neighbor_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.neighbors_neighbor_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: neighbors_neighbor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.neighbors_neighbor_id_seq OWNED BY public.neighbors.neighbor_id;


--
-- Name: plot_owners; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.plot_owners (
    plot_no integer NOT NULL,
    neighbor_id bigint NOT NULL
);


--
-- Name: plots; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.plots (
    plot_no integer NOT NULL,
    area_sq_m integer,
    lep_restricted boolean DEFAULT false NOT NULL,
    status text DEFAULT ''::text NOT NULL
);


--
-- Name: neighbors neighbor_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.neighbors ALTER COLUMN neighbor_id SET DEFAULT nextval('public.neighbors_neighbor_id_seq'::regclass);


--
-- Name: neighbors neighbors_last_name_first_name_middle_name_phone_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.neighbors
    ADD CONSTRAINT neighbors_last_name_first_name_middle_name_phone_key UNIQUE (last_name, first_name, middle_name, phone);


--
-- Name: neighbors neighbors_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.neighbors
    ADD CONSTRAINT neighbors_pkey PRIMARY KEY (neighbor_id);


--
-- Name: plot_owners plot_owners_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.plot_owners
    ADD CONSTRAINT plot_owners_pkey PRIMARY KEY (plot_no, neighbor_id);


--
-- Name: plots plots_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.plots
    ADD CONSTRAINT plots_pkey PRIMARY KEY (plot_no);


--
-- Name: plot_owners plot_owners_neighbor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.plot_owners
    ADD CONSTRAINT plot_owners_neighbor_id_fkey FOREIGN KEY (neighbor_id) REFERENCES public.neighbors(neighbor_id) ON DELETE CASCADE;


--
-- Name: plot_owners plot_owners_plot_no_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.plot_owners
    ADD CONSTRAINT plot_owners_plot_no_fkey FOREIGN KEY (plot_no) REFERENCES public.plots(plot_no) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

\unrestrict DLdoguJbcXkH7ppZpq6LtXU0eeHdZLHV4BFYZ8pgseegFHBrAtwcuwhNTlDNdvK

